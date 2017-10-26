from django.contrib import admin

# Register your models here.
from tiempo.models.alquiler import Alquilerr


@admin.register(Alquilerr)
class AlquilerAdmin(admin.ModelAdmin):
    pass
