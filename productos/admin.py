from django.contrib import admin
from .models import Categoria, Proveedor, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'creado_en']
    search_fields = ['nombre']


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'contacto', 'telefono', 'email', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre', 'contacto']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'categoria', 'proveedor', 'stock_actual', 'stock_minimo', 'precio_venta', 'activo']
    list_filter = ['categoria', 'activo', 'unidad_medida']
    search_fields = ['nombre', 'codigo']
    readonly_fields = ['creado_en', 'actualizado_en']
