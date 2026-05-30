from django import forms
from .models import Producto, Categoria, Proveedor


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre', 'codigo', 'descripcion', 'categoria', 'proveedor',
            'precio_compra', 'precio_venta', 'stock_actual', 'stock_minimo',
            'unidad_medida', 'imagen',
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput, forms.FileInput)):
                field.widget.attrs.setdefault('class', 'form-control')
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto', 'telefono', 'email', 'direccion', 'activo']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'activo':
                field.widget.attrs.setdefault('class', 'form-control')
