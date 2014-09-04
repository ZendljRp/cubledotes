# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields
from django.conf import settings
import core.files
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('status', models.PositiveIntegerField(default=0, choices=[(0, 'Draft'), (1, 'Scheduled'), (2, 'Published')])),
                ('title', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('scheduled_at', models.DateTimeField(null=True, blank=True)),
                ('outstanding_image', easy_thumbnails.fields.ThumbnailerImageField(null=True, blank=True, upload_to=core.files.UploadToDir('images'))),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(related_name='posts', to='tags.Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
