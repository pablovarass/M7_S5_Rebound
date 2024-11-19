from django.db import models


class Fabrica(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.TextField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=100)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre

