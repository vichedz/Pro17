from django.db import models
# Create your models here.


class Area(models.Model):
    nombre_del_area = models.CharField(max_length=100)
    descripcion = models.TextField()


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    dui = models.CharField(max_length=10)


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)


class Venta(models.Model):
    fecha_venta = models.DateField()
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
