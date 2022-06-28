from django.db import models

class Clientes(models.Model):
    
    nombre_fantasia = models.CharField(max_length=40)
    razon_social = models.CharField(max_length=40)
    cuit = models.IntegerField()
    calle = models.CharField(max_length=40)
    altura = models.IntegerField()
    fecha_alta = models.DateField()


class Proveedores(models.Model):
    
    nombre_fantasia = models.CharField(max_length=40)
    razon_social = models.CharField(max_length=40)
    cuit = models.IntegerField()
    calle = models.CharField(max_length=40)
    altura = models.IntegerField()
    fecha_alta = models.DateField()


class Articulos(models.Model):

    codigo = models.IntegerField()
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return f"Codigo: {self.codigo} - Nombre: {self.nombre} - Precio: {self.precio} - Stock: {self.stock}"

class Pagos(models.Model):
    monto = models.IntegerField()
    forma_pago = models.CharField(max_length=40)
    fecha_pago = models.DateField()

