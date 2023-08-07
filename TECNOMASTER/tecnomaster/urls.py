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
from publico import views as publico 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("marcas/", views.marcas, name="marcas"),
    path("add_marcas/", views.add_marcas, name="add_marcas"),
    path('marcas_chart/', views.marcas_chart, name='marcas_chart'),
    path('estadoUsuario_chart/', views.estadoUsuario_chart, name='estadoUsuario_chart'),
    path("edit_marcas/<int:id_marca>", views.edit_marcas, name="edit_marcas"),
    path("delete_marcas/<int:id_marca>", views.delete_marcas, name="delete_marcas"),
    #################################################################
    path("productos/", views.productos, name="productos"),
    path("add_productos/", views.add_productos, name="add_productos"),
    path("edit_productos/<int:id_producto>", views.edit_productos, name="edit_productos"),
    path("delete_productos/<int:id_producto>", views.delete_productos, name="delete_productos"),
    path('reporte_producto/<int:producto_id>/', views.reporte_producto, name='reporte_producto'),
    #################################################################
    path("usuarios/", views.usuarios, name="usuarios"),
    path('reporte-usuarios/', views.generar_reporte_usuario_pdf, name='reporte_usuarios'),
    path("add_usuarios/", views.add_usuarios, name="add_usuarios"), 
    path("edit_usuarios/<int:id_usuario>", views.edit_usuarios, name="edit_usuarios"),
    path("delete_usuarios/<int:id_usuario>", views.delete_usuarios, name="delete_usuarios"),   
    
    ################################################################# 
    path("valoraciones", views.valoraciones, name="valoraciones"),
    path("add_valoraciones/", views.add_valoraciones, name="add_valoraciones"),
    path("edit_valoraciones/<int:id_valoracion>", views.edit_valoraciones, name="edit_valoraciones"),
    path("delete_valoraciones/<int:id_valoracion>", views.delete_valoraciones, name="delete_valoraciones"),
     
    #################################################################
    path("categorias/", views.categorias, name="categorias"),
    path('reporte-categorias/', views.reporte_categorias, name='reporte_categorias'),
    path('categorias_chart/', views.categorias_chart, name='categorias_chart'),
    path("add_categorias/", views.add_categorias, name="add_categorias"),
    path("edit_categorias/<int:categoria_id>", views.edit_categorias, name="edit_categorias"),
    path("delete_categorias/<int:categoria_id>", views.delete_categorias, name="delete_categorias"),
    
    #################################################################
    path("dashboard/", views.dashboard, name="dashboard"),
    
    #################################################################
    path("pedidos/", views.pedidos, name="pedidos"),
    path("add_pedidos/", views.add_pedidos, name="add_pedidos"),
    path("edit_pedidos/<int:pedido_id>", views.edit_pedidos, name="edit_pedidos"),
    path("delete_pedidos/<int:pedido_id>", views.delete_pedidos, name="delete_pedidos"),
    
    #################################################################
    path("login", views.index, name="index"),
    
    #################################################################
    path("clientes", views.clientes, name="clientes"),
    path("clientes_chart/", views.clientesCharts, name="clientes_chart"),
    path('reporte_cliente/<int:cliente_id>/', views.generar_reporte_cliente_pdf, name='reporte_cliente_pdf'),
    path("add_cliente/", views.add_cliente, name="add_cliente"),
    path("edit_cliente/<int:cliente_id>", views.edit_cliente, name="edit_cliente"),
    path("delete_cliente/<int:cliente_id>", views.delete_cliente, name="delete_cliente"),
    
    #################################################################
    #PUBLICO
    #################################################################
    
    path("carrito_pagina/<int:id_producto>", publico.carrito_pagina, name="carrito_pagina"),
    #############################################
    path("categorias_pagina", publico.categorias_pagina, name="categorias_pagina"),
    #############################################
    path("detalle_producto_pagina/<int:producto_id>", publico.detalle_producto_pagina, name="detalle_producto_pagina"),
    #############################################
    path("", publico.index_pagina, name="index_pagina"),
    #############################################
    path("inicio_sesion_pagina", publico.inicio_sesion_pagina, name="inicio_sesion_pagina"),
    #############################################
    path("marcas_pagina", publico.marcas_pagina, name="marcas_pagina"),
    #############################################
    path("productos_nuevos_pagina", publico.productos_nuevos_pagina, name="productos_nuevos_pagina"),
    #############################################
    path("productos_ofertas_pagina", publico.productos_ofertas_pagina, name="productos_ofertas_pagina"),
    #############################################
    path("productos-categoria_pagina/<int:categoria_id>", publico.productos_categoria_pagina, name="productos-categoria_pagina"),
    #############################################
    path("sobre_nosotros_pagina", publico.sobre_nosotros_pagina, name="sobre_nosotros_pagina"),
    #############################################
    path("ultimas_compras_pagina", publico.ultimas_compras_pagina, name="ultimas_compras_pagina"),
    #############################################
    path("add_valoracion/<int:id_producto>", publico.add_valoracion, name="add_valoracion"),
    #############################################
    path("add_pedido/<int:id_producto>", publico.add_pedido, name="add_pedido"),
    
   
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    