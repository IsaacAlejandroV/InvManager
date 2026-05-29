from django.urls import path
from . import views

app_name = 'movimientos'

urlpatterns = [
    path('', views.MovimientoListView.as_view(), name='lista'),
    path('nuevo/', views.MovimientoCreateView.as_view(), name='crear'),
    path('alertas/', views.AlertasView.as_view(), name='alertas'),
]
