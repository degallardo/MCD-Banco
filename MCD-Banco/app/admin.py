from django.contrib import admin
from .models import Pais, Estado, Municipio, Sucursal, TipoTarjeta, SolicitudCredito, Promotor, Comision

admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Sucursal)
admin.site.register(TipoTarjeta)
admin.site.register(SolicitudCredito)
admin.site.register(Promotor)
admin.site.register(Comision)