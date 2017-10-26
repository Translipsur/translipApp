from django.db import models
from uuid import uuid4

from transBack.models.persona import Persona


class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    persona = models.ForeignKey(Persona)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __unicode__(self):
        return self.id
