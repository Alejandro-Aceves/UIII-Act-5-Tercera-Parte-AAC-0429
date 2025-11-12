from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_personal, name='inicio_personal'),

    # CLIENTES
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),

    # EMPLEADOS
    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),

    # VENTAS
    path('ventas/', views.ver_ventas, name='ver_ventas_personal'),
    path('ventas/agregar/', views.agregar_venta, name='agregar_venta_personal'),
    path('ventas/actualizar/<int:id>/', views.actualizar_venta, name='actualizar_venta_personal'),
    path('ventas/borrar/<int:id>/', views.borrar_venta, name='borrar_venta_personal'),
]
