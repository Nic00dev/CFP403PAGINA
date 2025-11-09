from django.db import models

# Create your models here.
class Proyecto_pruebas(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class tareas_prueba (models.Model):
    prueba = models.TextField(max_length=200);
    numero_prueba = models.IntegerField(20);