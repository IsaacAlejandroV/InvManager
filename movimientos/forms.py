from django import forms
from .models import MovimientoInventario
from productos.models import Producto


class MovimientoForm(forms.ModelForm):
    class Meta:
        model = MovimientoInventario
        fields = ['producto', 'tipo', 'cantidad', 'precio_unitario', 'notas']
        widgets = {
            'notas': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, tipo_inicial=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].queryset = Producto.objects.filter(activo=True).order_by('nombre')
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            elif not isinstance(field.widget, forms.Textarea):
                field.widget.attrs.setdefault('class', 'form-control')
            else:
                field.widget.attrs.setdefault('class', 'form-control')
        if tipo_inicial:
            self.fields['tipo'].initial = tipo_inicial

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad is not None and cantidad <= 0:
            raise forms.ValidationError('La cantidad debe ser mayor a cero.')
        return cantidad
