from django.urls import path
from .views import home, productos, crearp

urlpatterns = [
    path('', home,name="home"),
     path('productos/', productos,name="productos"),
     path('crear/', crearp, name="crearp" ),
]