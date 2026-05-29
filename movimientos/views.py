from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import F
from .models import MovimientoInventario
from .forms import MovimientoForm
from productos.models import Producto


class MovimientoListView(LoginRequiredMixin, ListView):
    model = MovimientoInventario
    template_name = 'movimientos/lista.html'
    context_object_name = 'movimientos'
    paginate_by = 25

    def get_queryset(self):
        qs = MovimientoInventario.objects.select_related('producto', 'usuario')
        tipo = self.request.GET.get('tipo', '')
        pid = self.request.GET.get('producto', '')
        if tipo:
            qs = qs.filter(tipo=tipo)
        if pid:
            qs = qs.filter(producto_id=pid)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['productos'] = Producto.objects.filter(activo=True)
        ctx['tipo_sel'] = self.request.GET.get('tipo', '')
        ctx['producto_sel'] = self.request.GET.get('producto', '')
        return ctx


class MovimientoCreateView(LoginRequiredMixin, CreateView):
    model = MovimientoInventario
    form_class = MovimientoForm
    template_name = 'movimientos/form.html'
    success_url = reverse_lazy('movimientos:lista')

    _TITULOS = {
        'entrada': ('Registrar Entrada de Stock', 'success'),
        'salida':  ('Registrar Salida de Stock',  'danger'),
        'ajuste':  ('Registrar Ajuste de Stock',  'warning'),
    }

    def _tipo(self):
        return self.request.GET.get('tipo', 'entrada')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['tipo_inicial'] = self._tipo()
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        titulo, color = self._TITULOS.get(self._tipo(), ('Registrar Movimiento', 'primary'))
        ctx['titulo'] = titulo
        ctx['color'] = color
        return ctx

    def form_valid(self, form):
        movimiento = form.save(commit=False)
        movimiento.usuario = self.request.user
        producto = movimiento.producto
        movimiento.stock_anterior = producto.stock_actual

        if movimiento.tipo == 'entrada':
            producto.stock_actual += movimiento.cantidad
        elif movimiento.tipo == 'salida':
            if producto.stock_actual < movimiento.cantidad:
                form.add_error(
                    'cantidad',
                    f'Stock insuficiente. Disponible: {producto.stock_actual} {producto.get_unidad_medida_display()}.'
                )
                return self.form_invalid(form)
            producto.stock_actual -= movimiento.cantidad
        elif movimiento.tipo == 'ajuste':
            producto.stock_actual = movimiento.cantidad

        movimiento.stock_posterior = producto.stock_actual
        producto.save()
        movimiento.save()

        messages.success(
            self.request,
            f'{movimiento.get_tipo_display()} registrada: {producto.nombre} '
            f'({movimiento.stock_anterior} → {movimiento.stock_posterior} {producto.get_unidad_medida_display()})'
        )
        return redirect(self.success_url)


class AlertasView(LoginRequiredMixin, ListView):
    template_name = 'movimientos/alertas.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return (
            Producto.objects
            .filter(activo=True, stock_actual__lte=F('stock_minimo'))
            .select_related('categoria', 'proveedor')
            .order_by('stock_actual')
        )
