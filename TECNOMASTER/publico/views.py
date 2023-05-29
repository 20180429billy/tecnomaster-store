import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from privado.models import *
from django.core.files.storage import FileSystemStorage

# Create your views here. 

def carrito_pagina(request, id_producto):
    productos = Producto.objects.get(id = id_producto)
    return render(request, "carrito_pagina.html",{
        'productos':productos
    })

####################################################################

def productos_categoria_pagina(request, categoria_id):
    categoria = Categoria.objects.get(id = categoria_id)
    productos = Producto.objects.filter(id_categoria = categoria_id)
    marca = Marcas.objects.all()
    
    return render(request, "productos-categoria_pagina.html", {
        'productos' : productos,
        'marca': marca,
        'categoria' : categoria
    })

####################################################################

def categorias_pagina(request):
    categorias = Categoria.objects.all().order_by("id")
    return render(request, "categorias_pagina.html", {
        "categorias" : categorias
    })

####################################################################

def detalle_producto_pagina(request, producto_id):
    productos = Producto.objects.get(id = producto_id)
    valoraciones = Valoraciones.objects.filter(id_producto = producto_id)
    return render(request, "detalle_producto_pagina.html", {
        'productos': productos,
        'valoraciones' : valoraciones
    })

####################################################################

def add_valoracion(request, id_producto):
    if request.method == "POST":
        valoracion = Valoraciones()
        valoracion.calificacion = request.POST["valoracion"]
        valoracion.comentario = request.POST["comentario"]
        valoracion.id_producto = Producto.objects.get(id = id_producto)

        valoracion.save()
        return redirect("detalle_producto_pagina",id_producto)
    else:
        return redirect("detalle_producto_pagina",id_producto)

####################################################################

def add_pedido(request, id_producto):
    if request.method == "POST":
        pedido = Pedido()
        pedido.id_producto = Producto.objects.get(id = id_producto)
        pedido.precio_pedido = request.POST["total_compra-precio"]
        pedido.cantidad = request.POST["cantidad"]

        pedido.save()
        return redirect("ultimas_compras_pagina")
    else:
        return redirect("ultimas_compras_pagina")

####################################################################

def index_pagina(request):
    return render(request, "index_pagina.html")

####################################################################

def inicio_sesion_pagina(request):
    return render(request, "inicio_sesion_pagina.html")

####################################################################

def marcas_pagina(request):
    return render(request, "marcas_pagina.html")

####################################################################

def productos_nuevos_pagina(request):
    return render(request, "productos_nuevos_pagina.html")

####################################################################

def productos_ofertas_pagina(request):
    return render(request, "productos_ofertas_pagina.html")



####################################################################

def sobre_nosotros_pagina(request):
    return render(request, "sobre_nosotros_pagina.html")

####################################################################

def ultimas_compras_pagina(request):
    pedidos = Pedido.objects.all()
    return render(request, "ultimas_compras_pagina.html",{
        'pedidos':pedidos
    })