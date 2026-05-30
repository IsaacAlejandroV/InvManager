from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    # Productos
    path('', views.ProductoListView.as_view(), name='lista'),
    path('nuevo/', views.ProductoCreateView.as_view(), name='crear'),
    path('<int:pk>/', views.ProductoDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='eliminar'),
    # Categorías
    path('categorias/', views.CategoriaListView.as_view(), name='categorias_lista'),
    path('categorias/nueva/', views.CategoriaCreateView.as_view(), name='categorias_crear'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categorias_editar'),
    path('categorias/<int:pk>/eliminar/', views.CategoriaDeleteView.as_view(), name='categorias_eliminar'),
    # Proveedores
    path('proveedores/', views.ProveedorListView.as_view(), name='proveedores_lista'),
    path('proveedores/nuevo/', views.ProveedorCreateView.as_view(), name='proveedores_crear'),
    path('proveedores/<int:pk>/editar/', views.ProveedorUpdateView.as_view(), name='proveedores_editar'),
    path('proveedores/<int:pk>/eliminar/', views.ProveedorDeleteView.as_view(), name='proveedores_eliminar'),
]
