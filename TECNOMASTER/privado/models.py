from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, verbose_name="Descripcion")
    image = models.ImageField(null=True, upload_to="articles")

    def __str__(self):
        return self.nombre  

    def delete(self, usign=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
       
       
class EstadoCliente(models.Model):
    estado_cliente = models.CharField(max_length=150)
    
    def __str__(self):
        return self.estado_cliente
    
     
class Cliente(models.Model):
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    dui = models.IntegerField()
    correo = models.CharField(max_length=150)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=250)
    clave = models.CharField(max_length=150)
    usuario = models.CharField(max_length=150)
    id_estado = models.ForeignKey(EstadoCliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombres




    
class TipoUsuario(models.Model):
    tipo_usuario = models.CharField(max_length=150, default="") 
    descripcion_tipo_usuario = models.CharField(max_length=250, default="")
    
    def __str__(self):
        return self.tipo_usuario
    

class EstadoUsuario(models.Model):
    estado_usuario = models.CharField(max_length=150, default="")

    def __str__(self):
        return self.estado_usuario


class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    apellido_usuario = models.CharField(max_length=100)
    correo_usuario = models.CharField(max_length=150)
    alias_usuario = models.CharField(max_length=100)
    clave_usuario = models.CharField(max_length=100)
    id_estado_usuario = models.ForeignKey(EstadoUsuario, on_delete=models.CASCADE)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_usuario
        
class Marcas(models.Model):
    marca = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to="articles")

    def __str__(self):
        return self.marca


class EstadoProducto(models.Model):
    estado_producto = models.CharField(max_length=100)

    def __str__(self):
        return self.estado_producto
    



class Producto(models.Model):
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100)
    descripcion_producto = models.CharField(max_length=100)
    precio_producto = models.IntegerField()
    imagen_producto = models.ImageField(null=True, upload_to="articles")
    especificaciones_producto = models.CharField(max_length=100)
    descuento = models.IntegerField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    id_estado_producto = models.ForeignKey(EstadoProducto, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.nombre_producto


class ImagenProducto(models.Model):
    imagen_producto = models.ImageField(null=True, upload_to="articles")
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.imagen_producto


class EstadoPedido(models.Model):
    estado_pedido = models.CharField(max_length=100)

    def __str__(self):
        return self.estado_pedido
    
class Pedido(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now=True, null=True, blank=True)
    direccion_pedido = models.CharField(max_length=200)
    id_estado = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_pedido = models.IntegerField()

    def __str__(self):
        return self.direccion_pedido

class EstadoValoracion(models.Model):
    estado_valoracion = models.CharField(max_length=100)

    def __str__(self):
        return self.estado_valoracion

class Valoracion(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, default="")
    calificacion = models.IntegerField()
    comentario = models.CharField(max_length=250)
    fecha = models.DateTimeField(auto_now=True)
    id_estado = models.ForeignKey(EstadoValoracion, on_delete=models.CASCADE)

    def __str__(self):
        return self.comentario

    
    
    
    
    

    
    