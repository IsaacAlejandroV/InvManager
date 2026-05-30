from django.db import models


class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=100, unique=True)
    descripcion = models.TextField('Descripción', blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']


class Proveedor(models.Model):
    nombre = models.CharField('Nombre', max_length=200)
    contacto = models.CharField('Contacto', max_length=100, blank=True)
    telefono = models.CharField('Teléfono', max_length=20, blank=True)
    email = models.EmailField('Email', blank=True)
    direccion = models.TextField('Dirección', blank=True)
    activo = models.BooleanField('Activo', default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']


class Producto(models.Model):
    UNIDADES = [
        ('pza', 'Pieza'),
        ('kg', 'Kilogramo'),
        ('lt', 'Litro'),
        ('mt', 'Metro'),
        ('caja', 'Caja'),
        ('paq', 'Paquete'),
    ]
    nombre = models.CharField('Nombre', max_length=200)
    codigo = models.CharField('Código', max_length=50, unique=True)
    descripcion = models.TextField('Descripción', blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='productos', verbose_name='Categoría'
    )
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='productos', verbose_name='Proveedor'
    )
    precio_compra = models.DecimalField('Precio de compra', max_digits=10, decimal_places=2, default=0)
    precio_venta = models.DecimalField('Precio de venta', max_digits=10, decimal_places=2, default=0)
    stock_actual = models.IntegerField('Stock actual', default=0)
    stock_minimo = models.IntegerField('Stock mínimo', default=5)
    unidad_medida = models.CharField('Unidad de medida', max_length=10, choices=UNIDADES, default='pza')
    activo = models.BooleanField('Activo', default=True)
    imagen = models.ImageField('Imagen', upload_to='productos/', blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} [{self.codigo}]"

    @property
    def stock_bajo(self):
        return self.stock_actual <= self.stock_minimo

    @property
    def valor_total(self):
        return self.stock_actual * self.precio_compra

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']
