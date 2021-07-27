"""
Definition of models.
"""

from django.db import models
from datetime import date

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=50)
    idPais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING, verbose_name = "Pais")

    def __str__(self):
        return '%s - %s' % (self.nombre, self.idPais)

class Municipio(models.Model):
    nombre = models.CharField(max_length=50)
    idEstado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING, verbose_name = "Estado")

    def __str__(self):
        return '%s - %s' % (self.nombre, self.idEstado)

class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    calle_y_numero = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    idPais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING, default=None, verbose_name = "Pais")
    idEstado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING, default=None, verbose_name = "Estado")
    idMunicipio = models.ForeignKey(Municipio, on_delete=models.DO_NOTHING, default=None, verbose_name = "Municipio")
    region = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.nombre)

class StatusPromotor(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % (self.nombre)

class Promotor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    idStatusPromotor = models.ForeignKey(StatusPromotor, on_delete=models.DO_NOTHING, default=None, verbose_name = "Estatus")
    fecha = models.DateField(auto_now=True)
    objetivo = models.IntegerField()
    porcentaje_comision = models.IntegerField()
    idSucursal = models.ForeignKey(Sucursal, on_delete=models.DO_NOTHING, default=None, verbose_name = "Sucursal")

    def __str__(self):
        return '%s %s' % (self.apellidos, self.nombre)

class TipoTarjeta(models.Model):
    nombre = models.CharField(max_length=50)
    tasa_interes = models.DecimalField(max_digits=2, decimal_places=2, default=None)

    def __str__(self):
        return '%s - Costo: %s' % (self.nombre, self.costo)

class TipoCredito(models.Model):
    nombre = models.CharField(max_length=50)
    tasa_interes = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return '%s - Tasa de interes: %s' % (self.nombre, self.tasa_interes)

class StatusSolicitudCredito(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % (self.nombre)

class Cliente(models.Model):
    fecha_alta = models.DateField(default=date.today)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    calle_y_numero = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    idPais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING, verbose_name = "Pais")
    idEstado = models.ForeignKey(Estado, on_delete=models.DO_NOTHING, verbose_name = "Estado")
    idMunicipio = models.ForeignKey(Municipio, on_delete=models.DO_NOTHING, verbose_name = "Municipio")
    fecha_nacimiento = models.DateField(null=True)
    cantidad_hijos = models.IntegerField()
    rfc = models.CharField(max_length=13)
    idPromotor = models.ForeignKey(Promotor, on_delete=models.DO_NOTHING, verbose_name = "Promotor")

    def __str__(self):
        return 'Nombre: %s Apellidos: %s' % (self.nombre)

# Cliente debe ir antes de SolicitudCredito.

class SolicitudCredito(models.Model):
    monto_solicitado = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    fecha_solicitud = models.DateField(default=date.today)
    idTipoCredito = models.ForeignKey(TipoCredito, on_delete=models.DO_NOTHING, default=None, verbose_name = "Tipo de credito")
    idStatusSolicitudCredito = models.ForeignKey(StatusSolicitudCredito, on_delete=models.DO_NOTHING, default=None, verbose_name = "Estatus")

    def __str__(self):
        return '%s - %s' % (self.nombre, self.tipo_credito)

class StatusCredito(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % (self.nombre)

class Credito(models.Model):
    fecha_alta = models.DateField(default=date.today)
    idCliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, verbose_name = "Cliente")
    idTipoCredito = models.ForeignKey(TipoCredito, on_delete=models.DO_NOTHING, verbose_name = "Tipo credito")
    monto_otorgado = models.DecimalField(max_digits=7, decimal_places=2)
    idStatusCredito = models.ForeignKey(StatusCredito, on_delete=models.DO_NOTHING, verbose_name = "Estatus")
    idSolicitud = models.ForeignKey(SolicitudCredito, on_delete=models.DO_NOTHING, verbose_name = "Solicitud")
    monto_pago = models.DecimalField(max_digits=7, decimal_places=2)
    dia_pago = models.PositiveSmallIntegerField()

    def __str__(self):
        return 'Fecha alta: %s Cliente: %s Tipo de credito: %s Monto otorgado: %s, Estatus: %s, Dia de pago: %s' % (self.fecha_alta, self.idCliente, self.idTipoCredito, self.monto_otorgado, self.status, self.dia_pago)

class Pagos(models.Model):
    idCredito = models.ForeignKey(Credito, on_delete=models.DO_NOTHING, verbose_name = "Credito")
    fecha_pago = models.DateField(default=date.today)
    monto_pagado = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return 'Credito: %s Fecha de pago: %s Monto pagado: %s' % (self.idCredito, self.fecha_pago, self.monto_pagado)

class Comision(models.Model):
    idPromotor = models.ForeignKey(Promotor, on_delete=models.DO_NOTHING, verbose_name = "Promotor")
    fecha = models.DateField(default=date.today)
    monto_colocado = models.DecimalField(max_digits=7, decimal_places=2)
    comision_ganada = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return 'Promotor: %s Fecha: %s, Monto Colocado: %s Comision ganada: %s' % (self.promotor, self.fecha, self.monto_colocado, self.comision_ganada)

class AyudaCovid(models.Model):
    fecha_solicitud = models.DateField(default=date.today)
    idCliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, verbose_name = "Cliente")
    motivo = models.TextField()
    fecha_aprobacion = models.DateField(null=True)
    apoyo_aprobado = models.PositiveIntegerField() # En meses para pagar el crédito

    def __str__(self):
        return 'Fecha de solicitud: %s Cliente: %s, Motivo: %s Fecha aprobacion: %s apoyo aprobado (en meses)' % (self.fecha_solicitud, self.idCliente, self.motivo, self.fecha_aprobacion, self.apoyo_aprobado)

# ToDo: Calificaciones_Internas, Calificaciones_Buro
