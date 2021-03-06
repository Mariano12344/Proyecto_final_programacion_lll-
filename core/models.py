from django.db import models

# Create your models here.

class Genero(models.Model):
    #id -> numero autoincrementable
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

#python manage.py makemigrations <---- lee el archivo models y crea un archivo de migracion 
#python manage.py migrate <---- tomar las migraciones pendientes y volcarlas contra la BBDD
#python manage.py createsuperuser

class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    duracion = models.IntegerField()
    anio = models.IntegerField(verbose_name="Año")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    sinopsis = models.TextField(null=True, blank=True)
    fecha_estreno = models.DateField(null=True, blank=True)  
    imagen = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre


