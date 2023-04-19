from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(default="", max_length=100)
    descripcion = models.CharField(max_length=255, verbose_name="Descripcion")
    image = models.ImageField(null=True, upload_to="articles")

    def __str__(self):
        return self.nombre 