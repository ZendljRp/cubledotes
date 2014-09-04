# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields
from django.conf import settings
import django.utils.timezone
import core.files


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=75)),
                ('company', models.CharField(null=True, blank=True, max_length=128, verbose_name='Empresa')),
                ('title', models.CharField(max_length=128, verbose_name='Nombre del proyecto')),
                ('stage', models.IntegerField(default=0, verbose_name='Etapa del proyecto', choices=[(0, 'Nuevo Proyecto'), (1, 'Retomar Proyecto')])),
                ('type', models.IntegerField(default=1, verbose_name='Tipo de proyecto', choices=[(0, 'Comercio Electrónico'), (1, 'Plataforma Web'), (2, 'Backend App'), (3, 'Gestión Servidores'), (5, 'Otro')])),
                ('other_type', models.CharField(null=True, blank=True, max_length=128, verbose_name='En caso de ser otro tipo de proyecto, especifica cual')),
                ('about', models.TextField(verbose_name='Acerca del proyecto (en que consiste, a quién va dirigido, etc.)')),
                ('hosting', models.BooleanField(default=False, verbose_name='¿Ya tienes hosting?')),
                ('hosting_assistance', models.BooleanField(default=False, verbose_name='¿Necesitas asesoramiento para contratar el hosting?')),
                ('hosting_type', models.IntegerField(blank=True, default=3, verbose_name='¿Que hosting quieres contratar?', choices=[(0, 'Amazon Web Services'), (1, 'Rackspace'), (2, 'Otro'), (3, 'No lo se')])),
                ('hosting_quotes', models.CharField(null=True, blank=True, choices=[('100', '100'), ('200', '200'), ('300', '300'), ('Más de 300', 'Más de 300')], verbose_name='¿Cuál es tu presupuesto mensual para el hosting?', max_length=128)),
                ('branding_design', models.BooleanField(default=True, verbose_name='¿Necesitas que diseñemos tu identidad corporativa?')),
                ('branding_design_about', models.TextField(blank=True, default='', verbose_name='Hablanos un poco sobre el diseño de identidad que quieres para el proyecto')),
                ('web_design', models.BooleanField(default=True, verbose_name='¿Necesitas que diseñemos tu sitio web?')),
                ('web_design_stage', models.IntegerField(blank=True, default=0, verbose_name='Etapa del diseño', choices=[(0, 'Nuevo'), (1, 'Rediseño')])),
                ('responsive_web_design', models.NullBooleanField(verbose_name='¿Necesitas diseño responsive para tu sitio web?')),
                ('badget', models.CharField(choices=[('2000-4000', '2.000 - 4.000'), ('4000-6000', '4.000 - 6.000'), ('6000-8000', '6.000 - 8.000'), ('Más de 8000', 'Más de 8.000')], verbose_name='¿Qué presupuesto tienes disponible para el proyecto?', max_length=128)),
                ('badget_file', models.FileField(null=True, blank=True, upload_to=core.files.UploadToDir('badgets'), verbose_name='Si dispones de un briefing del proyecto no dudes en enviárlo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('status', models.PositiveIntegerField(default=0, choices=[(0, 'Draft'), (1, 'Scheduled'), (2, 'Published')])),
                ('title', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('scheduled_at', models.DateTimeField(null=True, blank=True)),
                ('outstanding_image', easy_thumbnails.fields.ThumbnailerImageField(null=True, blank=True, upload_to=core.files.UploadToDir('images'))),
                ('description', models.TextField(null=True)),
                ('thumbnail_image', easy_thumbnails.fields.ThumbnailerImageField(null=True, blank=True, upload_to=core.files.UploadToDir('images'))),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(related_name='projects', to='tags.Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
