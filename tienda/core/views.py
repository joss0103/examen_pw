from django.shortcuts import render
from .models import Producto
from .forms import FormsProducto

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
    data = {
        'form': FormsProducto()
    }

    if request.method == 'POST':
        formulario = FormsProducto(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            
        else:
            data["form"] = formulario
    return render(request, 'core/crearproducto.html', data)

