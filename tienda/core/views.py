from django.shortcuts import render, redirect, get_object_or_404

from .Carrito import Carrito
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

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idproducto=producto_id)    
    carrito.agregar(producto)
    return redirect("productos")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idproducto=producto_id)
    carrito.eliminar(producto)
    return redirect("productos")

def restar_producto(request, producto_id):    
    carrito = Carrito(request)
    producto = Producto.objects.get(idproducto=producto_id)
    carrito.restar(producto)
    return redirect("productos")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("productos")    


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

