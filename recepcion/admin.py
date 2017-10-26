from django.contrib import admin
from .models.unidad import Unidad


# Register your models here.
@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    pass
