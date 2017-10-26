from django.contrib import admin

# Register your models here.
from .models.personal import Personale


@admin.register(Personale)
class PersonalAdmin(admin.ModelAdmin):
    pass
