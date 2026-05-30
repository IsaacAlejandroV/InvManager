from django.db.models import F


def alertas_stock(request):
    if request.user.is_authenticated:
        try:
            from productos.models import Producto
            count = Producto.objects.filter(
                activo=True, stock_actual__lte=F('stock_minimo')
            ).count()
            return {'alertas_count': count}
        except Exception:
            pass
    return {'alertas_count': 0}
