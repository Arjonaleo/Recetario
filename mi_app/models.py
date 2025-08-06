from django.db import models


# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.nombre}"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_compra = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"