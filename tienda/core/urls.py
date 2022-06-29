from django.urls import path
from .views import home, productos, crearp, edit_product, contacto, perfil

urlpatterns = [
    path('', home,name="home"),
     path('productos/', productos,name="productos"),
     path('crear/', crearp, name="crearp" ),
     path('actualizar/<id>/', edit_product, name="edit_product"), 
<<<<<<< Updated upstream
     path('contacto/', contacto, name="contacto"), 
     path('perfil/', perfil, name="perfil"),
=======
 
>>>>>>> Stashed changes
]