from email import message

from django.contrib import messages
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404

from .Carrito import Carrito
from .models import Producto
from .forms import FormsProducto, CustomUserCreationForm
from django.contrib.auth import authenticate, login


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

def contacto(request):
    return render(request,'core/contacto.html')


def perfil(request):
    return render(request,'core/perfil.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario    

    return render(request,'registration/registro.html', data)