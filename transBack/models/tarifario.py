from django.db import models
from uuid import uuid4


class Tarifario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(u'Nombre del tarifario', max_length=50)
    costo = models.DecimalField(u'Costo', max_digits=5, decimal_places=2)
    unidadMedida = models.CharField(u'Unidad de Medida', max_length=50)
    descripcion = models.CharField(u'Descripcion', max_length=50)

    class Meta:
        verbose_name = "Tarifario"
        verbose_name_plural = "Tarifarios"

    def __str__(self):
        return self.nombre
