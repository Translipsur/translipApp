from django.contrib import admin

# Register your models here.
from .models.alquiler import Alquiler
from .models.cliente import Cliente
from .models.persona import Persona
from .models.personal import Personal
from .models.proovedor import Proovedor
from .models.ruta import Ruta
from .models.soat import Soat
from .models.tarifario import Tarifario
from .models.unidades import Unidad


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    pass


@admin.register(Alquiler)
class AlquilerAdmin(admin.ModelAdmin):
    pass


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    pass


@admin.register(Proovedor)
class ProovedorAdmin(admin.ModelAdmin):
    pass


@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    pass


@admin.register(Soat)
class SoatAdmin(admin.ModelAdmin):
    pass


@admin.register(Tarifario)
class TarifarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    pass
