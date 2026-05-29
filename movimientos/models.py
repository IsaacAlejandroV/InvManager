from django.db import models
from django.conf import settings


class MovimientoInventario(models.Model):
    TIPOS = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
        ('ajuste', 'Ajuste'),
    ]
    producto = models.ForeignKey(
        'productos.Producto', on_delete=models.CASCADE,
        related_name='movimientos', verbose_name='Producto'
    )
    tipo = models.CharField('Tipo', max_length=10, choices=TIPOS)
    cantidad = models.IntegerField('Cantidad')
    stock_anterior = models.IntegerField('Stock anterior')
    stock_posterior = models.IntegerField('Stock posterior')
    precio_unitario = models.DecimalField(
        'Precio unitario', max_digits=10, decimal_places=2, default=0
    )
    notas = models.TextField('Notas', blank=True)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, related_name='movimientos', verbose_name='Usuario'
    )
    fecha = models.DateTimeField('Fecha', auto_now_add=True)

    def __str__(self):
        return (
            f"{self.get_tipo_display()} | {self.producto.nombre} | "
            f"{self.cantidad} {self.producto.get_unidad_medida_display()}"
        )

    class Meta:
        verbose_name = 'Movimiento de Inventario'
        verbose_name_plural = 'Movimientos de Inventario'
        ordering = ['-fecha']
