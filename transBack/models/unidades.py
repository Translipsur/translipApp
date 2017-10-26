from django.db import models
from uuid import uuid4


class Unidad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    marca = models.CharField(u'Marca', max_length=50)
    placa = models.CharField(u'Placa', max_length=50)
    tipo = models.CharField(u'Tipo', max_length=50)

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidads"

    def __str__(self):
        return self.marca
