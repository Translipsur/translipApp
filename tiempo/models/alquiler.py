from django.db import models
from uuid import uuid4

from transBack.models.alquiler import Alquiler
from transBack.models.unidades import Unidad


class Alquilerr(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    unidad = models.ForeignKey(Unidad)
    fechaIni = models.DateField(u'Fecha Inicio')
    fechaFin = models.DateField(u'Fecha Fin')
    alquiler = models.ForeignKey(Alquiler)

    class Meta:
        verbose_name = "Alquilerr"
        verbose_name_plural = "Alquilerrs"

    def __unicode__(self):
        return self.id
