from django.db import models
from uuid import uuid4

from transBack.models.personal import Personal


class Personale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    funcion = models.CharField(u'Funcion', max_length=50)
    estado = models.BooleanField(u'Estado', default=True)
    personales = models.ForeignKey(Personal)

    class Meta:
        verbose_name = "Personale"
        verbose_name_plural = "Personales"

    def __str__(self):
        return self.funcion
