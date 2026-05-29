from django.contrib import admin
from .models import MovimientoInventario


@admin.register(MovimientoInventario)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ['producto', 'tipo', 'cantidad', 'stock_anterior', 'stock_posterior', 'usuario', 'fecha']
    list_filter = ['tipo', 'fecha']
    search_fields = ['producto__nombre', 'producto__codigo']
    readonly_fields = ['stock_anterior', 'stock_posterior', 'fecha']
    date_hierarchy = 'fecha'
