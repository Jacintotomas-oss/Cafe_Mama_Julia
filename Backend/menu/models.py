from django.db import models
from datetime import date

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length= 250)
    orden = models.PositiveIntegerField(default=0, help_text="Menor número aparece primero")

    class Meta:
        ordering = ["orden", "nombre"]
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

def __str__(self):
    return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length= 250)
    descripcion = models.TextField(blank= True )
    precio = models.DecimalField(max_digits= 6, decimal_places= 2)
    foto = models.ImageField(upload_to= "productos", blank= True, null= True)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE, related_name= "productos")
    disponible = models.BooleanField(default= True)
    destacado = models.BooleanField(default= False)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "producto"
        verbose_name_plural = "productos"

def __str__(self):
    return self.nombre

class Promocion (models.Model):
    titulo = models.CharField(max_length= 250)
    descripcion = models.TextField(blank= True)
    image = models.ImageField(upload_to= "promociones", blank= True, null= True)
    fecha_inicio = models.DateField(default=date.today)
    fecha_fin = models.DateField(default=date.today)
    PromoActiva = models.BooleanField(default= True)

    class Meta:
        ordering = ["titulo"]
        verbose_name = "promoción"
        verbose_name_plural = "promociones"
def __str__(self):
    return self.titulo

class Info_Local(models.Model):
    Direccion = models.CharField(max_length= 250)
    Telefono = models.CharField(max_length= 250)
    horario = models.CharField(max_length= 250)
    instagram = models.CharField(max_length= 250)
    mapa_url = models.URLField(max_length= 250, blank= True, null= True)

def __str__(self):
    return self.Direccion