from django.shortcuts import render, redirect, get_object_or_404
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

def edit_product(request, id):

    productos = get_object_or_404(Producto, idproducto=id)

    data = {
        'form': FormsProducto(instance=productos)
    }

    if request.method == 'POST':
        formulario = FormsProducto(data=request.POST, instance=productos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="home")
        data["form"] = formulario
            

    return render(request, 'core/actualizar.html', data)

def contacto(request):
    return render(request,'core/contacto.html')


def perfil(request):
    return render(request,'core/perfil.html')