from django.contrib import admin
from .models import Pais, Estado, Municipio, Sucursal, TipoTarjeta, SolicitudCredito, Promotor, Comision, TipoCredito, StatusSolicitudCredito, Cliente, StatusCredito, Credito, Pagos, AyudaCovid, StatusPromotor, TarjetaCredito

admin.site.register(Pais)
#admin.site.register(Estado)
@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'idPais']

#admin.site.register(Municipio)
@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'idEstado']

#admin.site.register(Sucursal)
@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'calle_y_numero', 'colonia', 'idMunicipio', 'idEstado', 'idPais']
    list_filter = ('idMunicipio', 'idEstado', 'idPais')
    search_fields = ['nombre', 'calle_y_numero', 'colonia']

#admin.site.register(TipoTarjeta)
@admin.register(TipoTarjeta)
class TipoTarjetaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tasa_interes']
    #list_filter = ('idMunicipio', 'idEstado', 'idPais', 'region')
    #search_fields = ['nombre', 'calle_y_numero', 'colonia']

#admin.site.register(SolicitudCredito)
@admin.register(SolicitudCredito)
class SolicitudCreditoAdmin(admin.ModelAdmin):
    list_display = ['idCliente', 'monto_solicitado', 'fecha_solicitud', 'idTipoCredito', 'idStatusSolicitudCredito']
    list_filter = ('idTipoCredito', 'idStatusSolicitudCredito')
    search_fields = ['idCliente', 'fecha_solicitud']

#admin.site.register(Promotor)
@admin.register(Promotor)
class PromotorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellidos', 'idStatusPromotor', 'objetivo', 'porcentaje_comision']
    list_filter = ('idStatusPromotor', 'objetivo', 'porcentaje_comision')
    search_fields = ['nombre', 'apellidos']

admin.site.register(Comision)
admin.site.register(TipoCredito)
admin.site.register(StatusSolicitudCredito)

#admin.site.register(Cliente)
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellidos', 'fecha_alta', 'calle_y_numero', 'colonia', 'idMunicipio', 'idEstado', 'idPais', 'fecha_nacimiento', 'cantidad_hijos', 'rfc']
    list_filter = ('idMunicipio', 'idEstado', 'idPais')
    search_fields = ['nombre', 'apellidos', 'fecha_alta', 'fecha_nacimiento', 'cantidad_hijos', 'rfc']

admin.site.register(StatusCredito)

#admin.site.register(Credito)
@admin.register(Credito)
class CreditoAdmin(admin.ModelAdmin):
    list_display = ['fecha_alta', 'idCliente', 'idTipoCredito', 'monto_otorgado', 'idStatusCredito', 'idSolicitud', 'monto_pago', 'dia_pago']
    list_filter = ('idTipoCredito', 'idStatusCredito', 'dia_pago')
    search_fields = ['fecha_alta', 'idCliente']

admin.site.register(Pagos)

#admin.site.register(AyudaCovid)
@admin.register(AyudaCovid)
class AyudaCovidAdmin(admin.ModelAdmin):
    list_display = ['fecha_solicitud', 'idCliente', 'fecha_aprobacion', 'apoyo_aprobado']
    list_filter = ['apoyo_aprobado']
    search_fields = ['fecha_solicitud', 'fecha_aprobacion', 'idCliente']

admin.site.register(StatusPromotor)

@admin.register(TarjetaCredito)
class TarjetaCreditoAdmin(admin.ModelAdmin):
    list_display = ['idTipoTarjeta', 'idCredito', 'num_tarjeta', 'fecha', 'limite_credito']
    list_filter = ('idTipoTarjeta', 'limite_credito')
    search_fields = ['num_tarjeta']

#admin.site.register()
#admin.site.register()
#admin.site.register()
#admin.site.register()
#admin.site.register()
#admin.site.register()
#admin.site.register()
#admin.site.register()
#admin.site.register()
#admin.site.register()
#admin.site.register()
#admin.site.register()
#admin.site.register()
#admin.site.register()
#admin.site.register()
#admin.site.register()
#admin.site.register()


#class PaisAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None, {'fields': ['nombre']})
#    ]
#    list_display = ('nombre',)
#    list_filter = ('nombre',)
#    ordering = ('nombre',)
