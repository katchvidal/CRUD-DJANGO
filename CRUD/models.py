from django.db import models

# Create your models here.

class Persona(models.Model):
    #   Clave Primaria AutoIncremental
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=150)
    correo = models.EmailField('Email', max_length=255, unique=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ["apellido"]
    
    def __str__(self):
        return self.nombre
    