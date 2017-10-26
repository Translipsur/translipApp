from django.db import models
from uuid import uuid4

from transBack.models.persona import Persona


class Proovedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    persona = models.ForeignKey(Persona)

    class Meta:
        verbose_name = "Proovedor"
        verbose_name_plural = "Proovedors"

    def __unicode__(self):
        return self.id
