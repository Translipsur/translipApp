from django.db import models
from uuid import uuid4

from transBack.models.alquiler import Alquiler
from transBack.models.persona import Persona


class Personal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    persona = models.ForeignKey(Persona)
    alquiler = models.ForeignKey(Alquiler)

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personals"

    def __unicode__(self):
        return self.id
