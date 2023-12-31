from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
         return self.nombre +' '+ self.apellido

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_legajo = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    def __str__(self):
         return self.nombre +' '+ self.apellido

class Servicio(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0.0)
    activo = models.BooleanField(default=True)
    def __str__(self):
         return self.nombre
        
        
class Coordinador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    numero_documento = models.IntegerField(blank=False)
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
         return self.nombre +' '+ self.apellido
    
class ReservaServicio(models.Model):
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_reserva = models.DateField(null=False)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    responsable = models.ForeignKey(Coordinador,on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio,on_delete=models.CASCADE)
    precio = models.IntegerField(default=0)