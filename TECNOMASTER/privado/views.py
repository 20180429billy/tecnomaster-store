import io
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.core.files.storage import FileSystemStorage
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.shortcuts import get_object_or_404
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from django.db.models import Count



# Create your views here.
#get_object_or_404 

#===============================MARCAS====================================

def marcas(request):
    marcas = Marcas.objects.all().order_by("id")
    context = {
        "marcas" : marcas
    }
    return render(request, "marcas.html", context) 

def add_marcas(request):
    if request.method == "POST" and request.FILES['image']:
        marca = Marcas()
        marca.marca = request.POST["marca"]
        marca.image = request.FILES["image"]
        marca.save()
        return redirect("marcas")
    else:
        return redirect("marcas")

def edit_marcas(request, id_marca):
    marca = Marcas.objects.get(id = id_marca)
    
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(marca.image):
                os.remove(marca.image.path)
            marca.image = request.FILES["image"]

        marca.marca = request.POST["marca"]
        marca.save()
        return redirect("marcas")
    else:
        return redirect("marcas")
    
def delete_marcas(request, id_marca):
    marca = Marcas.objects.get(id = id_marca)
    marca.delete()
    return redirect("marcas")

#============================================================================
#===============================PRODUCTOS====================================

def productos(request):
    productos = Producto.objects.all().order_by("id")
    categorias = Categoria.objects.all().order_by("id")
    estados = EstadoProducto.objects.all().order_by("id")
    marcas = Marcas.objects.all().order_by("id")
    usuarios = Usuario.objects.all().order_by("id")
    
    context = {
        "productos" : productos,
        "categorias" : categorias,
        "estados" : estados,
        "marcas" : marcas,
        "usuarios" : usuarios
    }
    
    return render(request, "productos.html", context)

def add_productos(request):
    
    if request.method == "POST" and request.FILES["image"]:
        producto = Producto()
        id_categoria = request.POST["id_categoria"]
        producto.id_categoria = Categoria.objects.get(id = id_categoria)
        producto.nombre_producto = request.POST["nombre"]
        producto.descripcion_producto = request.POST["descripcion"]
        producto.precio_producto = request.POST["precio"]
        producto.imagen_producto = request.FILES["image"]
        producto.especificaciones_producto = request.POST["especificaciones"]
        producto.descuento = request.POST["descuento"]
        id_usuario = request.POST["id_usuario"]
        id_marca = request.POST["id_marca"]
        id_estado = request.POST["id_estado"]
        producto.id_usuario = Usuario.objects.get(id = id_usuario)
        producto.id_marca = Marcas.objects.get(id = id_marca)
        producto.id_estado_producto = EstadoProducto.objects.get(id = id_estado)
        producto.save()
        return redirect("productos")
    else:
        return redirect("productos")


def  edit_productos(request, id_producto):
    producto = Producto.objects.get(id = id_producto)
    
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(producto.imagen_producto):
                os.remove(producto.imagen_producto.path)
            producto.imagen_producto = request.FILES['image']
            
            
        id_categoria = request.POST["id_categoria"]
        producto.id_categoria = Categoria.objects.get(id = id_categoria)
        producto.nombre_producto = request.POST["nombre"]
        producto.descripcion_producto = request.POST["descripcion"]
        producto.precio_producto = request.POST["precio"]
        producto.especificaciones_producto = request.POST["especificaciones"]
        producto.descuento = request.POST["descuento"]
        id_usuario = request.POST["id_usuario"]
        id_marca = request.POST["id_marca"]
        id_estado = request.POST["id_estado"]
        producto.id_usuario = Usuario.objects.get(id = id_usuario)
        producto.id_marca = Marcas.objects.get(id = id_marca)
        producto.id_estado_producto = EstadoProducto.objects.get(id = id_estado)
        producto.save()
        return redirect("productos")
    else:
        return redirect("productos")
    
def delete_productos(request, id_producto):
    producto = Producto.objects.get(id = id_producto)
    producto.delete()
    return redirect("productos")

def reporte_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    # Crear un objeto PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reporte_producto_{producto_id}.pdf"'

    # Crear el contenido del PDF
    buffer = io.BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)

    # Agregar contenido al PDF
    data = [
        ["ID de Categoría:", producto.id_categoria.nombre],
        ["Nombre del Producto:", producto.nombre_producto],
        ["Descripción del Producto:", producto.descripcion_producto],
        ["Precio del Producto:", producto.precio_producto],
        ["Especificaciones del Producto:", producto.especificaciones_producto],
        ["Marca del Producto:", producto.id_marca.marca],
    ]

    # Obtener la imagen del producto
    try:
        image_file = producto.imagen_producto.path
    except Exception as e:
        # Si ocurre un error al cargar la imagen, simplemente muestra un mensaje
        image_file = "Imagen no disponible"

    # Agregar la imagen al contenido
    data.append(["Imagen del producto:", ""])
    data[-1][-1] = Image(image_file, width=100, height=100)

    # Estilos de tabla y párrafo
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.royalblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    table = Table(data, colWidths=[150, 390])
    table.setStyle(style)

    # Crear el documento PDF y agregar la tabla
    elements = [Paragraph(f"Reporte de producto: {producto.nombre_producto}", getSampleStyleSheet()['Heading1'])]
    elements.append(table)

    # Generar el PDF
    pdf.build(elements)

    # Obtener el contenido del buffer y cerrarlo
    pdf_buffer = buffer.getvalue()
    buffer.close()

    # Escribir el contenido del PDF en la respuesta
    response.write(pdf_buffer)

    return response



#============================================================================
#===============================USUARIOS====================================

def usuarios(request):
    tipo_usuario = TipoUsuario.objects.all()
    estado_usuario = EstadoUsuario.objects.all()
    usuario = Usuario.objects.all().order_by("id")

    context = {
        "tipoUsuarios" : tipo_usuario,
        "estadoUsuarios" : estado_usuario,
        "usuarios": usuario
    }
    return render(request, "usuarios.html", context)

def add_usuarios(request):
    if request.method == "POST":
        usuario = Usuario()
        usuario.nombre_usuario = request.POST["nombres"]
        usuario.apellido_usuario  = request.POST["apellidos"]
        usuario.correo_usuario = request.POST["correo"]
        usuario.alias_usuario = request.POST["alias"]
        usuario.clave_usuario = request.POST["clave"]
        estado_usuario = request.POST["id_estado_usuario"]
        tipo_usuario = request.POST["id_tipo_usuario"]
        usuario.id_estado_usuario = EstadoUsuario.objects.get(id = estado_usuario)
        usuario.id_tipo_usuario = TipoUsuario.objects.get(id = tipo_usuario)
        usuario.save()
        return redirect("usuarios")
    else:
        return redirect("usuarios")
        
def edit_usuarios(request, id_usuario):
    usuario = Usuario.objects.get(id = id_usuario)

    if request.method == "POST":
        
        usuario.nombre_usuario = request.POST["nombres"]
        usuario.apellido_usuario  = request.POST["apellidos"]
        usuario.correo_usuario = request.POST["correo"]
        usuario.alias_usuario = request.POST["alias"]
        usuario.clave_usuario = request.POST["clave"]
        estado_usuario = request.POST["id_estado_usuario"]
        tipo_usuario = request.POST["id_tipo_usuario"]
        usuario.id_estado_usuario = EstadoUsuario.objects.get(id = estado_usuario)
        usuario.id_tipo_usuario = TipoUsuario.objects.get(id = tipo_usuario)
        usuario.save()
        return redirect("usuarios")
    else:
        return redirect("usuarios")

def delete_usuarios(request, id_usuario):
    usuario = Usuario.objects.get(id = id_usuario)
    usuario.delete()
    return redirect("usuarios")

#============================================================================
#===============================VALORACIONES====================================

def valoraciones(request):
    valoraciones = Valoraciones.objects.all().order_by("id")
    pedidos = Pedido.objects.all().order_by("id")
    estados = EstadoValoraciones.objects.all().order_by("id")

    context = {
        "valoraciones":valoraciones,
        "pedidos":pedidos,
        "estados":estados
    }
    return render(request, "valoraciones.html", context) 

def add_valoraciones(request):
    if request.method == "POST":
        valoracion = Valoraciones()
        valoracion.calificacion = request.POST["valoracion"]
        valoracion.comentario = request.POST["comentario"]
        id_estado = request.POST["id_estado"]
        
        id_pedido = request.POST["id_pedido"]
        valoracion.id_estado = EstadoValoraciones.objects.get(id = id_estado)
        valoracion.id_pedido = Pedido.objects.get(id = id_pedido)
        valoracion.save()
        return redirect("valoraciones")
    else:
        return redirect("valoraciones")

def edit_valoraciones(request, id_valoracion):
    valoracion = Valoraciones.objects.get(id = id_valoracion)

    if request.method == "POST":
        
        valoracion.calificacion = request.POST["valoracion"]
        valoracion.comentario = request.POST["comentario"]
        id_estado = request.POST["id_estado"]
        
        id_pedido = request.POST["id_pedido"]
        valoracion.id_estado = EstadoValoraciones.objects.get(id = id_estado)
        valoracion.id_pedido = Pedido.objects.get(id = id_pedido)
        valoracion.save()
        return redirect("valoraciones")
    else:
        return redirect("valoraciones")

def delete_valoraciones(request, id_valoracion):
    valoracion = Valoraciones.objects.get(id = id_valoracion)
    valoracion.delete()
    return redirect("valoraciones")


#============================================================================
#===============================PEDIDOS====================================

def pedidos(request):
    pedidos = Pedido.objects.all().order_by("id")
    estados = EstadoPedido.objects.all().order_by("id")
    clientes = Cliente.objects.all().order_by("id")
    productos = Producto.objects.all().order_by("id")
    context = {
        "pedidos" : pedidos,
        "estados": estados,
        "clientes" : clientes,
        "productos":productos
    }
    return render(request, "pedidos.html", context) 

def add_pedidos(request):

    if request.method == "POST":
        pedido = Pedido()
        id_cliente = request.POST["id_cliente"]
        pedido.id_cliente = Cliente.objects.get(id = id_cliente)
        id_estado = request.POST["id_estado"]
        pedido.id_estado = EstadoPedido.objects.get(id = id_estado)
        id_producto = request.POST["id_producto"]
        pedido.id_producto = Producto.objects.get(id = id_producto)
        pedido.direccion_pedido = request.POST["direccion"]
        pedido.cantidad = request.POST["cantidad"]
        pedido.precio_pedido = request.POST["precio"]
        pedido.save()
        return redirect("pedidos")
    else:
        return redirect("pedidos")

def edit_pedidos(request, pedido_id):
    pedido = Pedido.objects.get(id = pedido_id)
    if request.method == "POST":
        id_cliente = request.POST["id_cliente"]
        pedido.id_cliente = Cliente.objects.get(id = id_cliente)
        id_estado = request.POST["id_estado"]
        pedido.id_estado = EstadoPedido.objects.get(id = id_estado)
        id_producto = request.POST["id_producto"]
        pedido.id_producto = Producto.objects.get(id = id_producto)
        pedido.direccion_pedido = request.POST["direccion"]
        pedido.cantidad = request.POST["cantidad"]
        pedido.precio_pedido = request.POST["precio"]
        pedido.save()
        return redirect("pedidos")
    else:
        return redirect("pedidos")

def delete_pedidos(request, pedido_id):
    pedido = Pedido.objects.get(id = pedido_id)
    pedido.delete()
    return redirect("pedidos")


#=============================================================================
#===============================CATEGORIAS====================================
#

def add_categorias(request):
    if request.method == "POST" and request.FILES['image']:
        categoria = Categoria()
        categoria.nombre = request.POST["nombre"]
        categoria.descripcion = request.POST["descripcion"]
        categoria.image = request.FILES['image']
        categoria.save()
        return redirect("categorias")
    else:
        return redirect("categorias")
    
    
    
def edit_categorias(request, categoria_id):
    categoria = Categoria.objects.get(id = categoria_id)
    
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(categoria.image):
                os.remove(categoria.image.path)
            categoria.image = request.FILES['image']
        
        categoria.nombre = request.POST["nombre"]
        categoria.descripcion = request.POST["descripcion"]
        categoria.save()
        return redirect("categorias")
    else:
        return redirect("categorias")
    
    
    
def delete_categorias(request, categoria_id):
    categoria = Categoria.objects.get(id = categoria_id)
    categoria.delete()
    return redirect("categorias")
    
def marcas_chart(request):
    marcas = Marcas.objects.all().order_by("id")
    productos_por_marca = [marca.producto_set.count() for marca in marcas]

    context = {
        "marcas": marcas,
        "productos_por_marca": productos_por_marca,
    }

    return render(request, "marcas_chart.html", context)

def categorias_chart(request):
    categorias = Categoria.objects.all().order_by("id")
    productos_por_categoria = [categoria.producto_set.count() for categoria in categorias]

    context = {
        "categorias": categorias,
        "productos_por_categoria": productos_por_categoria,
    }

    return render(request, "categorias_chart.html", context)

def clientesCharts(request):
    estado = EstadoCliente.objects.all()
    clientes = Cliente.objects.all().order_by("id")

    # Obtener la cantidad de clientes activos e inactivos
    clientes_activos = clientes.filter(
        id_estado__estado_cliente="Activo").count()
    clientes_inactivos = clientes.filter(
        id_estado__estado_cliente="Inactivo").count()

    context = {
        "estados": estado,
        "clientes": clientes,
        "clientes_activos": clientes_activos,
        "clientes_inactivos": clientes_inactivos
    }

    return render(request, "clientes_chart.html", context)


def categorias(request):
    categorias = Categoria.objects.all().order_by("id")
    return render(request, "categorias.html", {
        "categorias" : categorias
    })

def reporte_categorias(request):
    # Obtener la información de las categorías y contar el número de productos
    categorias = Categoria.objects.annotate(num_productos=Count('producto'))

    # Generar el PDF con la información
    buffer = io.BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)

    # Contenido del PDF
    elements = [Paragraph("Reporte de Categorías", getSampleStyleSheet()['Heading1']), Spacer(1, 12)]

    # Estilos de tabla y párrafo
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.royalblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])

    # Crear la tabla con los datos de las categorías
    data = [['ID', 'Nombre de Categoría', 'Descripción', 'Número de Productos']]
    for categoria in categorias:
        data.append([categoria.id, categoria.nombre, categoria.descripcion, categoria.num_productos])

    table = Table(data, colWidths=[50, 150, 150, 150])
    table.setStyle(style)

    elements.append(table)

    # Generar el PDF
    pdf.build(elements)

    # Obtener el contenido del buffer y cerrarlo
    pdf_buffer = buffer.getvalue()
    buffer.close()

    # Escribir el contenido del PDF en la respuesta
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_categorias.pdf"'
    response.write(pdf_buffer)

    return response
    
#============================================================================
#===============================DASHBOARD====================================

def dashboard(request):
    return render(request, "dashboard.html")

#============================================================================
#===============================LOGIN====================================

def index(request):
    return render(request, "index.html")

#============================================================================
#===============================CLIENTES====================================

def clientes(request):
    estado = EstadoCliente.objects.all()
    clientes = Cliente.objects.all().order_by("id")
    context = {
        "estados":estado,
        "clientes": clientes
    }
    return render(request, "clientes.html", context)

def add_cliente(request):
    if request.method == "POST":
        cliente = Cliente()
        cliente.nombres = request.POST["nombres"]
        cliente.apellidos = request.POST["apellidos"]
        cliente.dui = request.POST["dui"]
        cliente.correo = request.POST["correo"]
        cliente.telefono = request.POST["telefono"]
        cliente.direccion = request.POST["direccion"]
        cliente.clave = request.POST["clave"]
        cliente.usuario = request.POST["usuario"]
        estado_cliente = request.POST["id_estado"]
        cliente.id_estado = EstadoCliente.objects.get(id = estado_cliente)
        cliente.save()
        return redirect("clientes")
    else:
        return redirect("clientes")
    
def edit_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id = cliente_id)
    
    if request.method == "POST":
        cliente.nombres = request.POST["nombres"]
        cliente.apellidos = request.POST["apellidos"]
        cliente.dui = request.POST["dui"]
        cliente.correo = request.POST["correo"]
        cliente.telefono = request.POST["telefono"]
        cliente.direccion = request.POST["direccion"]
        cliente.clave = request.POST["clave"]
        cliente.usuario = request.POST["usuario"]
        estado_cliente = request.POST["id_estado"]
        cliente.id_estado = EstadoCliente.objects.get(id = estado_cliente)
        cliente.save()
        return redirect("clientes")
    else:
        return redirect("clientes")
    
def delete_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id = cliente_id)
    cliente.delete()
    return redirect("clientes")

def generar_reporte_cliente_pdf(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    # Crear el archivo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reporte_cliente_{cliente.id}.pdf"'
    
    # Crear el canvas y agregar contenido
    p = canvas.Canvas(response, pagesize=letter)

    # Agregar un título con estilo
    p.setFont("Helvetica-Bold", 20)
    p.drawCentredString(300, 750, f"Reporte de Cliente  : {cliente.nombres} {cliente.apellidos}")

    # Crear una tabla para organizar la información
    data = [
        ["Nombres:", cliente.nombres],
        ["Apellidos:", cliente.apellidos],
        ["DUI:", cliente.dui],
        ["Correo:", cliente.correo],
        ["Teléfono:", cliente.telefono],
        ["Dirección:", cliente.direccion],
        ["Estado:", cliente.id_estado.estado_cliente],
    ]

    # Estilo de la tabla
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.royalblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
    ])

    # Crear la tabla
    width, height = letter
    table = Table(data, colWidths=[100, 440])
    table.setStyle(style)
    table.wrapOn(p, width, height)
    table.drawOn(p, 50, 600)


    p.showPage()
    p.save()
    
    return response

##reportes solano

def reporte_valoraciones(request):
    # Obtener la información de las valoraciones
    valoraciones = Valoraciones.objects.all()

    # Generar el PDF con la información
    buffer = io.BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)

    # Contenido del PDF
    elements = [Paragraph("Reporte de Valoraciones", getSampleStyleSheet()['Heading1']), Spacer(1, 12)]

    # Estilos de tabla y párrafo
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.royalblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])

    # Crear la tabla con los datos de las valoraciones
    data = [[' Producto', 'Calificación', 'Comentario', 'Fecha', 'Estado Valoración']]
    for valoracion in valoraciones:
        data.append([valoracion.id_producto.nombre_producto, valoracion.calificacion, valoracion.comentario,
                      valoracion.fecha.strftime("%d de %B de %Y"), valoracion.id_estado])

    table = Table(data, colWidths=[120, 120, 120, 120, 120])
    table.setStyle(style)

    elements.append(table)

    # Generar el PDF
    pdf.build(elements)

    # Obtener el contenido del buffer y cerrarlo
    pdf_buffer = buffer.getvalue()
    buffer.close()

    # Escribir el contenido del PDF en la respuesta
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_valoraciones.pdf"'
    response.write(pdf_buffer)

    return response
def reporte_pedido_pagado(request, pedido_id):
    # Obtener el pedido con el estado "Pagado" o devolver un error 404 si no existe
    pedido = get_object_or_404(Pedido, id=pedido_id, id_estado__estado_pedido='Pagado')

    # Crear un objeto PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reporte_pedido_{pedido_id}.pdf"'

    # Crear el contenido del PDF
    buffer = io.BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)

    # Agregar contenido al PDF
    data = [
        ["ID del Pedido:", pedido.id],
        ["ID del Cliente:", f"{pedido.id_cliente.nombres} {pedido.id_cliente.apellidos}"],
        ["Fecha del Pedido:", pedido.fecha_pedido.strftime("%d de %B del %Y")],
        ["Dirección del Pedido:", pedido.direccion_pedido],
        ["Estado del Pedido:", pedido.id_estado.estado_pedido],
        ["Cantidad:", pedido.cantidad],
        ["Precio del Pedido:", pedido.precio_pedido],
        ["Nombre del producto:", pedido.id_producto.nombre_producto],
    ]

    # Obtener la URL de la imagen del producto
    try:
        image_url = pedido.id_producto.imagen_producto.path
    except Exception as e:
        # Si ocurre un error al obtener la URL de la imagen, simplemente muestra un mensaje
        image_url = ""

    # Agregar la imagen al contenido
    data.append(["Imagen del producto:", ""])
    if image_url:
        data[-1][-1] = Image(image_url, width=100, height=100)

    # Estilos de tabla y párrafo
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.royalblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    table = Table(data, colWidths=[150, 390])
    table.setStyle(style)

    # Crear el documento PDF y agregar la tabla
    elements = [Paragraph(f"Factura del Pedido #{pedido.id}", getSampleStyleSheet()['Heading1'])]
    elements.append(table)

    # Generar el PDF
    pdf.build(elements)

    # Obtener el contenido del buffer y cerrarlo
    pdf_buffer = buffer.getvalue()
    buffer.close()

    # Escribir el contenido del PDF en la respuesta
    response.write(pdf_buffer)

    return response

def reporte_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    # Crear un objeto PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reporte_pedido_{pedido_id}.pdf"'

    # Crear el contenido del PDF
    buffer = io.BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)

    # Agregar contenido al PDF
    data = [
        ["ID del Pedido:", pedido.id],
        ["Nombre del Cliente:", f"{pedido.id_cliente.nombres} {pedido.id_cliente.apellidos}"],
        ["Fecha del Pedido:", pedido.fecha_pedido.strftime("%d de %B de %Y")],        
        ["Dirección del Pedido:", pedido.direccion_pedido],
        ["Dirección del Pedido:", pedido.direccion_pedido],
        ["Estado del Pedido:", pedido.id_estado.estado_pedido],
        ["ID del Producto:", pedido.id_producto.nombre_producto],
        ["Cantidad:", pedido.cantidad],
        ["Precio del Pedido:", pedido.precio_pedido],
    ]

    # Estilos de tabla y párrafo
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.royalblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    table = Table(data, colWidths=[150, 390])
    table.setStyle(style)

    # Crear el documento PDF y agregar la tabla
    elements = [Paragraph(f"Reporte del Pedido #{pedido.id}", getSampleStyleSheet()['Heading1'])]
    elements.append(table)

    # Generar el PDF
    pdf.build(elements)

    # Obtener el contenido del buffer y cerrarlo
    pdf_buffer = buffer.getvalue()
    buffer.close()

    # Escribir el contenido del PDF en la respuesta
    response.write(pdf_buffer)

    return response
    
        


