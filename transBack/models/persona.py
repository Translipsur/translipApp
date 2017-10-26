from django.db import models
from uuid import uuid4


class Persona(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(u'Nombre', max_length=50)
    apellidoP = models.CharField(u'Apellido Paterno', max_length=50)
    apellidoM = models.CharField(u'Apellido Materno', max_length=50)
    dni = models.CharField(u'DNI', max_length=50)
    direccion = models.CharField(u'Direccion', max_length=50)
    celular = models.CharField(u'Celular', max_length=50)
    ruc = models.CharField(u'RUC', max_length=50)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.nombre
