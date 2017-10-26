from django.db import models
from uuid import uuid4

from transBack.models.alquiler import Alquiler
from transBack.models.cliente import Cliente


class Unidad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    alquiler = models.ForeignKey(Alquiler)
    cliente = models.ForeignKey(Cliente)
    fecha = models.DateField(u'Fecha')
    estado = models.BooleanField(u'Estado', default=True)
    tipo = models.CharField(u'Tipo Unidad', max_length=50)

    class Meta:
        verbose_name = "Unidadd"
        verbose_name_plural = "Unidadds"

    def __str__(self):
        return self.tipo
