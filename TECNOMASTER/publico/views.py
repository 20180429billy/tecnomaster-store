from django.shortcuts import render

# Create your views here.

def carrito_pagina(request):
    return render(request, "carrito_pagina.html")

####################################################################

def categorias_pagina(request):
    return render(request, "categorias_pagina.html")

####################################################################

def detalle_producto_pagina(request):
    return render(request, "detalle_producto_pagina.html")

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

def productos_categoria_pagina(request):
    return render(request, "productos-categoria_pagina.html")

####################################################################

def sobre_nosotros_pagina(request):
    return render(request, "sobre_nosotros_pagina.html")

####################################################################

def ultimas_compras_pagina(request):
    return render(request, "ultimas_compras_pagina.html")