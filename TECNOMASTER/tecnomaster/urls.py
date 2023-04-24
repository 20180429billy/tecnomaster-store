"""tecnomaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from privado import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path("marcas/", views.marcas, name="marcas"),
    path("add_marcas/", views.add_marcas, name="add_marcas"),
    path("edit_marcas/<int:id_marca>", views.edit_marcas, name="edit_marcas"),
    path("delete_marcas/<int:id_marca>", views.delete_marcas, name="delete_marcas"),
    path("productos/", views.productos, name="productos"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("add_usuarios/", views.add_usuarios, name="add_usuarios"), 
    path("edit_usuarios/<int:id_usuario>", views.edit_usuarios, name="edit_usuarios"),
    path("delete_usuarios/<int:id_usuario>", views.delete_usuarios, name="delete_usuarios"),    
    path("valoraciones/", views.valoraciones, name="valoraciones"),
    path("categorias/", views.categorias, name="categorias"),
    path("add_categorias/", views.add_categorias, name="add_categorias"),
    path("edit_categorias/<int:categoria_id>", views.edit_categorias, name="edit_categorias"),
    path("delete_categorias/<int:categoria_id>", views.delete_categorias, name="delete_categorias"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("", views.index, name="index"),
    path("clientes", views.clientes, name="clientes"),
    path("add_cliente/", views.add_cliente, name="add_cliente"),
    path("edit_cliente/<int:cliente_id>", views.edit_cliente, name="edit_cliente"),
    path("delete_cliente/<int:cliente_id>", views.delete_cliente, name="delete_cliente")
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    