from django.db import models
from uuid import uuid4


class Ruta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    lugarOrigen = models.CharField(u'Lugar Origen', max_length=50)
    lugarDestino = models.CharField(u'Lugar Destino', max_length=50)
    distancia = models.CharField(u'Distancia', max_length=50)
    detalle = models.CharField(u'Detalle', max_length=50)

    class Meta:
        verbose_name = "Ruta"
        verbose_name_plural = "Rutas"

    def __str__(self):
        return self.lugarOrigen
