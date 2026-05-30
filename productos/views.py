from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q, F
from .models import Producto, Categoria, Proveedor
from .forms import ProductoForm, CategoriaForm, ProveedorForm


# ── Productos ──────────────────────────────────────────────────────────────────

class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'productos/lista.html'
    context_object_name = 'productos'
    paginate_by = 20

    def get_queryset(self):
        qs = Producto.objects.filter(activo=True).select_related('categoria', 'proveedor')
        q = self.request.GET.get('q', '').strip()
        cat = self.request.GET.get('categoria', '')
        bajo = self.request.GET.get('stock_bajo', '')
        if q:
            qs = qs.filter(Q(nombre__icontains=q) | Q(codigo__icontains=q))
        if cat:
            qs = qs.filter(categoria_id=cat)
        if bajo:
            qs = qs.filter(stock_actual__lte=F('stock_minimo'))
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categorias'] = Categoria.objects.all()
        ctx['q'] = self.request.GET.get('q', '')
        ctx['categoria_sel'] = self.request.GET.get('categoria', '')
        ctx['stock_bajo_filtro'] = self.request.GET.get('stock_bajo', '')
        return ctx


class ProductoDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = 'productos/detalle.html'
    context_object_name = 'producto'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['movimientos'] = self.object.movimientos.select_related('usuario').order_by('-fecha')[:20]
        return ctx


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/form.html'
    success_url = reverse_lazy('productos:lista')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titulo'] = 'Nuevo Producto'
        ctx['accion'] = 'Crear producto'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, f'Producto "{form.instance.nombre}" creado exitosamente.')
        return super().form_valid(form)


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/form.html'

    def get_success_url(self):
        return reverse_lazy('productos:detalle', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titulo'] = f'Editar: {self.object.nombre}'
        ctx['accion'] = 'Guardar cambios'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, 'Producto actualizado exitosamente.')
        return super().form_valid(form)


class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('productos:lista')

    def post(self, request, *args, **kwargs):
        producto = self.get_object()
        producto.activo = False
        producto.save()
        messages.success(request, f'Producto "{producto.nombre}" desactivado.')
        return redirect(self.success_url)


# ── Categorías ─────────────────────────────────────────────────────────────────

class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'productos/categorias/lista.html'
    context_object_name = 'categorias'


class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'productos/categorias/form.html'
    success_url = reverse_lazy('productos:categorias_lista')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titulo'] = 'Nueva Categoría'
        ctx['accion'] = 'Crear categoría'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, 'Categoría creada exitosamente.')
        return super().form_valid(form)


class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'productos/categorias/form.html'
    success_url = reverse_lazy('productos:categorias_lista')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titulo'] = f'Editar: {self.object.nombre}'
        ctx['accion'] = 'Guardar cambios'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, 'Categoría actualizada exitosamente.')
        return super().form_valid(form)


class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    success_url = reverse_lazy('productos:categorias_lista')

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        nombre = obj.nombre
        obj.delete()
        messages.success(request, f'Categoría "{nombre}" eliminada.')
        return redirect(self.success_url)


# ── Proveedores ────────────────────────────────────────────────────────────────

class ProveedorListView(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = 'productos/proveedores/lista.html'
    context_object_name = 'proveedores'

    def get_queryset(self):
        return Proveedor.objects.filter(activo=True)


class ProveedorCreateView(LoginRequiredMixin, CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'productos/proveedores/form.html'
    success_url = reverse_lazy('productos:proveedores_lista')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titulo'] = 'Nuevo Proveedor'
        ctx['accion'] = 'Crear proveedor'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, 'Proveedor creado exitosamente.')
        return super().form_valid(form)


class ProveedorUpdateView(LoginRequiredMixin, UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'productos/proveedores/form.html'
    success_url = reverse_lazy('productos:proveedores_lista')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titulo'] = f'Editar: {self.object.nombre}'
        ctx['accion'] = 'Guardar cambios'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, 'Proveedor actualizado exitosamente.')
        return super().form_valid(form)


class ProveedorDeleteView(LoginRequiredMixin, DeleteView):
    model = Proveedor
    success_url = reverse_lazy('productos:proveedores_lista')

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.activo = False
        obj.save()
        messages.success(request, f'Proveedor "{obj.nombre}" desactivado.')
        return redirect(self.success_url)
