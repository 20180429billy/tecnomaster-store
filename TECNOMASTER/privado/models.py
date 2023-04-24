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
    
class EstadoUsuario(models.Model):
    tipo_usuario = models.CharField(max_length=150) 
    descripcion_tipo_usuario = models.CharField(max_length=250)
    
    def __str__(self):
        return self.tipo_usuario
    
class TipoUsuario:
    estado_usuario = models.CharField(max_length=150)

    def __str__(self):
        return self.estado_usuario
    
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100, verbose_name="Nombre Usuario")
    apellido_usuario = models.CharField(max_length=100)
    correo_usuario = models.CharField(max_length=150)
    alias_usuario = models.CharField(max_length=100)
    clave_usuario = models.CharField(max_length=100)
    id_estado_usuario = models.ForeignKey(EstadoUsuario, on_delete=models.CASCADE)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    
    

    
    