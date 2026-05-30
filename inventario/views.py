from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, F
from django.utils import timezone
from productos.models import Producto
from movimientos.models import MovimientoInventario


@login_required
def dashboard(request):
    today = timezone.now().date()

    total_productos = Producto.objects.filter(activo=True).count()
    productos_stock_bajo = Producto.objects.filter(
        activo=True, stock_actual__lte=F('stock_minimo')
    ).count()
    valor_inventario = (
        Producto.objects.filter(activo=True)
        .aggregate(total=Sum(F('stock_actual') * F('precio_compra')))['total'] or 0
    )
    movimientos_hoy = MovimientoInventario.objects.filter(fecha__date=today).count()
    movimientos_recientes = (
        MovimientoInventario.objects
        .select_related('producto', 'usuario')
        .order_by('-fecha')[:10]
    )
    productos_alerta = (
        Producto.objects.filter(activo=True, stock_actual__lte=F('stock_minimo'))
        .select_related('categoria')
        .order_by('stock_actual')[:6]
    )

    context = {
        'total_productos': total_productos,
        'productos_stock_bajo': productos_stock_bajo,
        'valor_inventario': valor_inventario,
        'movimientos_hoy': movimientos_hoy,
        'movimientos_recientes': movimientos_recientes,
        'productos_alerta': productos_alerta,
    }
    return render(request, 'dashboard.html', context)
