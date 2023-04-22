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
    

    
    