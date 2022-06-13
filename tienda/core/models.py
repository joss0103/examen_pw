
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Categoria(models.Model):
    id_Categoria = models.IntegerField(primary_key=True, verbose_name='ID CATEGORIA:')
    categoria = models.CharField(default='NombreCategoria', max_length=25)

    def __str__(self):
        return self.categoria



class usuario(models.Model):
    usuario =  models.CharField(primary_key=True, max_length=35, verbose_name='USUARIO: ')
    contrasenia= models.CharField(max_length=15, verbose_name='CONTRASENIA: ')

class Producto(models.Model):
    serie_producto = models.CharField(primary_key=True, max_length=10)
    nombre_producto = models.CharField(max_length=30)
    descripcion = models.TextField()
    codigo = models.CharField(max_length=10)
    modelo = models.CharField(max_length=20)
    valor = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    valor_oferta = models.IntegerField(blank=True, null=True)
    oferta = models.BooleanField()
    nuevo = models.BooleanField()

    def __str__(self):
        return self.nombre_producto


class Pedido(models.Model):
    num_pedido = models.IntegerField(primary_key=True)
    despacho_domicilio = models.BooleanField()
    forma_pago = models.BooleanField()
    pedido_aceptado = models.BooleanField()
    direccion_despacho = models.CharField(max_length=70)
    numero_direccion = models.IntegerField()   
    producto = models.ManyToManyField(Producto)
 

    def __str__(self):
        return self.num_pedido

class Contacto(models.Model):
    nombre = models.CharField(max_length=25)
    email = models.CharField(max_length=35)
    consulta = models.TextField()

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    valor = models.IntegerField()
    fecha = models.DateTimeField(default=timezone.now)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, related_name='pedidoVenta')


    def __str__(self):
        return self.cliente
