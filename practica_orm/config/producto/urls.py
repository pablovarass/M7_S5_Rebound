from django.urls import path
from .views import (
    listar_productos,
    crear_producto,
    iniciar_sesion,
    home_page,
    cerrar_sesion,
    registro,
    editar_producto,
    eliminar_producto,
    crear_fabrica,
    listar_fabricas,
    editar_fabrica,
    eliminar_fabrica,
)

urlpatterns = [
    # Rutas de productos
    path('listar_productos/', listar_productos, name='listar_productos'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('editar_producto/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),

    # Rutas de fábricas
    path('crear_fabrica/', crear_fabrica, name='crear_fabrica'),
    path('listar_fabricas/', listar_fabricas, name='listar_fabricas'),
    path('editar_fabrica/<int:fabrica_id>/', editar_fabrica, name='editar_fabrica'),
    path('eliminar_fabrica/<int:fabrica_id>/', eliminar_fabrica, name='eliminar_fabrica'),

    # Rutas de autenticación y páginas generales
    path('registro/', registro, name='registro'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
    path('', home_page, name='home'),  # Ruta para el path vacío
    path('home/', home_page, name='home'),
    path('index/', home_page, name='index'),
]

