
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from django.utils import timezone
# Create your models here.
class Categoria(models.Model):
    id_Categoria = models.AutoField(primary_key=True, verbose_name='ID CATEGORIA:')
    categoria = models.CharField(default='NombreCategoria', max_length=25, verbose_name='CATEGORIA: ')

    def __str__(self):
        return self.categoria

class SubCategoria(models.Model):
    idSubcategoria = models.AutoField(primary_key=True, verbose_name='ID SUBCATEGORIA:')
    subCategoria= models.CharField(max_length=50, verbose_name='SUBCATEGORIA: ')


class cliente (models.Model):
    rut = models.CharField(primary_key=True, verbose_name= 'RUT: ')
    nombre=  models.CharField (max_length=50, verbose_name= 'NOMBRE: ')
    telefono = models.CharField(max_length=12, verbose_name='TELEFONO: ')
    correo= models.EmailField (max_length=80, verbose_name='CORREO ELECTRONICO: ' )
    suscripcion= models.BooleanField

class usuario(models.Model):
    usuario =  models.AutoField(primary_key=True, verbose_name='USUARIO: ')
    contrasenia= models.CharField(max_length=15, verbose_name='CONTRASENIA: ')

class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True, verbose_name='ID PRODUCTO:')
    nombre_producto = models.CharField(max_length=30, verbose_name= 'NOMBRE PRODUCTO: ')
    descripcion = models.TextField(max_length=200, verbose_name='DESCRIPCION: ')
    valor = models.IntegerField(max_length=10, verbose_name='VALOR: ')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    subcategoria=models.ForeignKey(SubCategoria, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    valor_oferta = models.IntegerField(blank=True, null=True, verbose_name='VALOR OFERTA: ')
    oferta = models.BooleanField(max_length= 10, verbose_name='OFERTA: ')
    stock = models.IntegerField(max_length= 100, verbose_name= 'STOCK: ')

    def __str__(self):
        return self.nombre_producto


class Pedido(models.Model):
    idpedido = models.AutoField(primary_key=True)
    despacho= models.BooleanField()
    forma_pago = models.BooleanField()
    pedido_aceptado = models.BooleanField()
    direccion_despacho = models.CharField(max_length=70)
    numero_direccion = models.IntegerField()   
    producto = models.ManyToManyField(Producto)
 

    def __str__(self):
        return self.num_pedido

class Contacto(models.Model):
    idcontacto = models.IntegerField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=25)
    email = models.CharField(max_length=35)
    consulta = models.TextField()

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    idventa= models.IntegerField(primary_key=True, max_length=25)
    valor = models.IntegerField()
    fecha = models.DateTimeField(default=timezone.now)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT, related_name='pedidoVenta')


    def __str__(self):
        return self.cliente

