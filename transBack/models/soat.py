from django.db import models
from uuid import uuid4


class Soat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    fechaIni = models.DateField(u'Fecha Inicio')
    fechaFin = models.DateField(u'Fecha Fin')
    estado = models.BooleanField(u'Estado', default=True)

    class Meta:
        verbose_name = "Soat"
        verbose_name_plural = "Soats"

    def __unicode__(self):
        return self.fechaIni
