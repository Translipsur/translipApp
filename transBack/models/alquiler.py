from django.db import models
from uuid import uuid4

from transBack.models.cliente import Cliente


class Alquiler(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cliente = models.ForeignKey(u'Cliente', Cliente)

    class Meta:
        verbose_name = "Alquiler"
        verbose_name_plural = "Alquilers"

    def __unicode__(self):
        return self.id
