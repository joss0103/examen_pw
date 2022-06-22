
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    id_Categoria = models.AutoField(primary_key=True, verbose_name='ID CATEGORIA:')
    categoria = models.CharField( max_length=25, verbose_name='CATEGORIA: ')

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
    suscripcion= models.BooleanField()

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    idventa= models.AutoField(primary_key=True)
    valortotal = models.ForeignKey(Pedido,on_delete=models.PROTECT)
    fecha = models.DateTimeField(default=timezone.now)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)


    def __str__(self):
        return self.cliente

class Comuna(models.Model):
    idComuna = models.AutoField(primary_key=True)
    nombreComuna = models.CharField(max_length=20, verbose_name='NOMBRE COMUNA: ' )

    def __str__(self):
        return self.nombreComuna

class Region(models.Model):
    idRegion = models.AutoField(primary_key=True)
    nombreRegion = models.CharField(max_length=20, verbose_name='NOMBRE REGION: ')

    def __str__(self):
        return self.nombreRegion


class Despacho(models.Model):
    idDespacho = models.AutoField(primary_key=True)
    nombreDespacho = models.CharField(max_length=25, verbose_name='NOMBRE RECEPTOR: ')
    direccionDespacho = models.CharField(max_length=25, verbose_name='DIRECCIÓN DESPACHO: ')
    nombreComuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    nombreRegion=models.ForeignKey(Region, on_delete=models.PROTECT)
    telefono = models.CharField(max_length=25)

    def __str__(self):
        return self.idDespacho        

class usuario(models.Model):
    usuario =  models.AutoField(primary_key=True, verbose_name='USUARIO: ')
    contrasenia= models.CharField(max_length=15, verbose_name='CONTRASENIA: ')

    def __str__(self):
        return self.usuario

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
    forma_pago = models.BooleanField(verbose_name='FORMA PAGO: ')
    estado_pedido = models.CharField( max_length=25, verbose_name='ESTADO PEDIDO: ')
    nombreDespacho = models.ForeignKey(Despacho, on_delete=models.PROTECT)
    direccionDespacho = models.ForeignKey(Despacho, on_delete=models.PROTECT)
    nombreComuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    nombreRegion=models.ForeignKey(Region, on_delete=models.PROTECT)
    telefono = models.ForeignKey(Despacho, on_delete=models.PROTECT)
    producto = models.ManyToManyField(Producto)
    fecha = models.ForeignKey(Venta, on_delete=models.PROTECT)
    cantidad = models.IntegerField(max_length=25, verbose_name='CANTIDAD: ')
    valor_total = models.IntegerField(max_length=25, verbose_name='VALOR TOTAL: ')
 

    def __str__(self):
        return self.idpedido

class Contacto(models.Model):
    idcontacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25, verbose_name='NOMBRE: ')
    email = models.CharField(max_length=35, verbose_name='EMAIL: ')
    consulta = models.TextField()

    def __str__(self):
        return self.nombre


