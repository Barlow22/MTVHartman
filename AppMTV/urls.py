from django.urls import path
from AppMTV import views

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('clientes/', views.clientes, name="Clientes"),
    path('proveedores/', views.proveedores, name="Proveedores"),
    path('articulos/', views.articulos, name="Articulos"),
    path('pagos/', views.pagos, name="Pagos"),
    path('buscar/', views.buscar),
]

