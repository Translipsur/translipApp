from django.contrib import admin

# Register your models here.
from .models.unidad import Unidade


@admin.register(Unidade)
class UnidadAdmin(admin.ModelAdmin):
    pass
