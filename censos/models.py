from django.db import models

class Censo(models.Model):
    nombre_completo = models.CharField(max_length=255)
    dni = models.CharField(max_length=20, unique=True)
    edad = models.IntegerField(null=True, blank=True)
    genero = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    estado_civil = models.CharField(max_length=20, blank=True, null=True)
    tiene_hijos = models.BooleanField(default=False)
    cantidad_hijos = models.IntegerField(null=True, blank=True)
    edades_hijos = models.TextField(blank=True, null=True)
    nivel_educativo = models.CharField(max_length=100, blank=True, null=True)
    ocupacion = models.CharField(max_length=100, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_completo