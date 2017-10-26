from django.db import models
from uuid import uuid4

from transBack.models.proovedor import Proovedor
from transBack.models.unidades import Unidad


class Unidade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    proveedor = models.ForeignKey(Proovedor)
    fechaIni = models.DateField(u'Fecha Inicio')
    fechaFin = models.DateField(u'Fecha Fin')
    costo = models.DecimalField(u'Costo', max_digits=5, decimal_places=2)
    unidad = models.ForeignKey(Unidad)

    class Meta:
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"

    def __unicode__(self):
        return self.id
