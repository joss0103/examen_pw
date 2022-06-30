from django.urls import path
from . import views
from .views import agregar_producto, eliminar_producto, home, limpiar_carrito, productos, crearp, edit_product, restar_producto, profile, registro


urlpatterns = [
    path('', home,name="home"),
     path('productos/', productos,name="productos"),
     path('crear/', crearp, name="crearp" ),
     path('actualizar/<id>/', edit_product, name="edit_product"),
     path('agregar/<int:producto_id>/', agregar_producto, name="Add"), 
     path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
     path('restar/<int:producto_id>/', restar_producto, name="Sub"),
     path('limpiar/', limpiar_carrito, name="CLS"),
     path('profile/', profile, name="users-profile"),
     path('registro/', registro, name="registro"),
]