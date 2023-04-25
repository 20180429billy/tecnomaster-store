from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Categoria)
admin.site.register(EstadoCliente)
admin.site.register(Cliente)
admin.site.register(EstadoUsuario)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Marcas)
admin.site.register(Producto)
admin.site.register(ImagenProducto)
admin.site.register(EstadoProducto)
admin.site.register(EstadoPedido)
admin.site.register(Pedido)
admin.site.register(Valoracion)
admin.site.register(EstadoValoracion)