"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=50)
    idPais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.nombre, self.idPais)

class Municipio(models.Model):
    nombre = models.CharField(max_length=50)
    idEstado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.nombre, self.idEstado)

class Sucursal(models.Model):
    nombre = models.CharField(max_length=50, default='Sucursal')
    calle_y_numero = models.CharField(max_length=50, default='Calle y No')
    colonia = models.CharField(max_length=50, default='Colonia')
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING, default='País')
    estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING, default='Estado')
    municipio = models.ForeignKey(Municipio, on_delete=models.DO_NOTHING, default='Municipio')
    region = models.CharField(max_length=50, default='Region')

    def __str__(self):
        return '%s' % (self.nombre)

class TipoTarjeta(models.Model):
    nombre = models.CharField(max_length=50, default='Tipo de tarjeta')
    costo = models.IntegerField()

    def __str__(self):
        return '%s - Costo: %s' % (self.nombre, self.costo)

class SolicitudCredito(models.Model):
    nombre = models.CharField(max_length=50, default='Tipo de crédito')
    costo = models.IntegerField()
    tasa_interes = models.IntegerField()

    def __str__(self):
        return '%s - %s' % (self.nombre, self.costo)

class Promotor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100, default='Apellidos')
    status = models.CharField(max_length=10)
    fecha = models.DateField(auto_now=True)
    objetivo = models.IntegerField()
    porcentaje_comision = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.apellidos, self.nombre)

class Comision(models.Model):
    promotor = models.ForeignKey(Promotor, on_delete=models.DO_NOTHING)
    fecha = models.DateField()
    monto_colocado = models.IntegerField()
    comision_ganada = models.IntegerField()

#class Cliente(models.Model):
#    nombre = models.CharField(max_length=100)
#    apellido_paterno = models.CharField(max_length=100, default='Apellido Paterno')
#    apellido_materno = models.CharField(max_length=100, default='Apellido Materno')
#    fecha_nacimiento = models.DateField()
#    calle_y_numero = models.CharField(max_length=50, default='Calle y No')
#    colonia = models.CharField(max_length=50, default='Colonia')
#    pais = models.ForeignKey(Pais, default='México', on_delete=models.DO_NOTHING)
#    estado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING)
#    municipio = models.ForeignKey(Municipio, on_delete=models.DO_NOTHING)
#    fecha_alta = models.DateField(auto_now_add=True, default='Fecha de alta')
#    rfc = models.CharField(max_length=13, default='RFC')

#    def __str__(self):
#        return '%s %s %s - %s' % (self.apellido_paterno, self.apellido_materno, self.nombre, self.rfc)

#class Cuenta(models.Model):
#    numero_cuenta = models.CharField(max_length=8)
#    idCliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
#    fecha = models.DateField(auto_now=True,)
#    saldo = models.DecimalField(max_digits=12, decimal_places=2)

#    def __str__(self):
#        return '%s - %s  %s  %s' % (self.numero_cuenta, self.idCliente, self.fecha, self.saldo)

