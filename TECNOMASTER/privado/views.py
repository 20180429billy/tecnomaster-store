import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.core.files.storage import FileSystemStorage

# Create your views here.
#get_object_or_404

#===============================MARCAS====================================

def marcas(request):
    marcas = Marcas.objects.all().order_by("id")
    context = {
        "marcas" : marcas
    }
    return render(request, "marcas.html", context) 

#============================================================================
#===============================PRODUCTOS====================================

def productos(request):
    return render(request, "productos.html")

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
    return render(request, "valoraciones.html") 

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
    
   

def categorias(request):
    categorias = Categoria.objects.all().order_by("id")
    return render(request, "categorias.html", {
        "categorias" : categorias
    })
    
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
    
        


