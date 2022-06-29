from django.urls import path
from .views import home, productos, crearp, edit_product

urlpatterns = [
    path('', home,name="home"),
     path('productos/', productos,name="productos"),
     path('crear/', crearp, name="crearp" ),
     path('actualizar/<id>/', edit_product, name="edit_product"), 
]