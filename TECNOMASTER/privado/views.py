from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Categoria
from django.core.files.storage import FileSystemStorage

# Create your views here.
#get_object_or_404

def marcas(request):
    return render(request, "marcas.html")

def productos(request):
    return render(request, "productos.html")

def usuarios(request):
    return render(request, "usuarios.html")

def valoraciones(request):
    return render(request, "valoraciones.html")

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
    if request.method == "POST":
        print(request.POST)
        categoria = Categoria.objects.get(id = categoria_id)
        categoria.nombre = request.POST["nombre"]
        categoria.descripcion = request.POST["descripcion"]
        
        if request.POST["image."] == "":
            categoria.save()
            return redirect("categorias")
        else:
            categoria.image = request.FILES['image']
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

def dashboard(request):
    return render(request, "dashboard.html")

def index(request):
    return render(request, "index.html")

