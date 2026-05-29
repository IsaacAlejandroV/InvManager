from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    ROLES = [
        ('admin', 'Administrador'),
        ('empleado', 'Empleado'),
    ]
    rol = models.CharField('Rol', max_length=10, choices=ROLES, default='empleado')
    telefono = models.CharField('Teléfono', max_length=20, blank=True)

    def es_admin(self):
        return self.rol == 'admin'

    def __str__(self):
        nombre = self.get_full_name()
        return nombre if nombre else self.username

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['username']
