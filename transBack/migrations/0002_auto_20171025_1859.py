# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 23:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import transBack.models.cliente
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('transBack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Alquiler',
                'verbose_name_plural': 'Alquilers',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transBack.Persona')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('alquiler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transBack.Alquiler')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transBack.Persona')),
            ],
            options={
                'verbose_name': 'Personal',
                'verbose_name_plural': 'Personals',
            },
        ),
        migrations.CreateModel(
            name='Proovedor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transBack.Persona')),
            ],
            options={
                'verbose_name': 'Proovedor',
                'verbose_name_plural': 'Proovedors',
            },
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lugarOrigen', models.CharField(max_length=50, verbose_name='Lugar Origen')),
                ('lugarDestino', models.CharField(max_length=50, verbose_name='Lugar Destino')),
                ('distancia', models.CharField(max_length=50, verbose_name='Distancia')),
                ('detalle', models.CharField(max_length=50, verbose_name='Detalle')),
            ],
            options={
                'verbose_name': 'Ruta',
                'verbose_name_plural': 'Rutas',
            },
        ),
        migrations.CreateModel(
            name='Soat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fechaIni', models.DateField(verbose_name='Fecha Inicio')),
                ('fechaFin', models.DateField(verbose_name='Fecha Fin')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Soat',
                'verbose_name_plural': 'Soats',
            },
        ),
        migrations.CreateModel(
            name='Tarifario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del tarifario')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Costo')),
                ('unidadMedida', models.CharField(max_length=50, verbose_name='Unidad de Medida')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tarifario',
                'verbose_name_plural': 'Tarifarios',
            },
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('placa', models.CharField(max_length=50, verbose_name='Placa')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidads',
            },
        ),
        migrations.AddField(
            model_name='alquiler',
            name='cliente',
            field=models.ForeignKey(on_delete=transBack.models.cliente.Cliente, to='transBack.Cliente'),
        ),
    ]
