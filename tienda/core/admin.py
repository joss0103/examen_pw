from django.contrib import admin
from .models import Contacto, Venta, Pedido, Producto, Despacho, Region,Comuna, SubCategoria, Categoria, Profile
# Register your models here.


admin.site.register(Contacto)
admin.site.register(Venta)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Despacho)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Profile)
admin.site.register(SubCategoria)
admin.site.register(Categoria)