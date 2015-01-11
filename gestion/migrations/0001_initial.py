# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmaceutico',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('age', models.DateField()),
                ('calleDeFarmacia', models.CharField(max_length=100)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name_plural': 'Farmaceutico',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('age', models.DateField()),
                ('hospital', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name_plural': 'Medicos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('age', models.DateField()),
                ('tarjeta_sanitaria', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name_plural': 'Pacientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('farmacos', models.CharField(max_length=100)),
                ('duracionDias', models.IntegerField()),
                ('unidades', models.IntegerField()),
                ('cadaCuantasHoras', models.IntegerField()),
                ('fecha', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('fechaDispensacion', models.DateTimeField(null=True, blank=True)),
                ('farmaceutico', models.ForeignKey(to='gestion.Farmaceutico', null=True)),
                ('medico', models.ForeignKey(to='gestion.Medico')),
                ('paciente', models.ForeignKey(to='gestion.Paciente', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name_plural': 'Recetas',
            },
            bases=(models.Model,),
        ),
    ]
