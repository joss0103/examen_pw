from django.shortcuts import render
from .models import Producto

# Create your views here.
def home(request):
    return render(request,'core/index.html')


def productos(request):
    productos = Producto.objects.all()
    data = { 
        'productos': productos
    }
    return render(request,'core/productos.html', data )


def crearp(request):
    return render(request, 'core/crearproducto.html')

