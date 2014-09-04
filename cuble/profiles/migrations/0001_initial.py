# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(max_length=30, verbose_name='username', unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
                ('email', models.EmailField(blank=True, verbose_name='email address', max_length=75)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('bio', models.TextField(blank=True, verbose_name='Description', null=True)),
                ('strength', models.PositiveIntegerField(verbose_name='Programming Python/Django', default=1)),
                ('dexterity', models.PositiveIntegerField(verbose_name='Programming Javascript/HTML5/CSS3', default=1)),
                ('constitution', models.PositiveIntegerField(verbose_name='Server Architecture', default=1)),
                ('intelligence', models.PositiveIntegerField(verbose_name='Software Design and Theory', default=1)),
                ('wisdom', models.PositiveIntegerField(verbose_name='Data Bases', default=1)),
                ('charisma', models.PositiveIntegerField(verbose_name='Management', default=1)),
                ('groups', models.ManyToManyField(blank=True, verbose_name='groups', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_query_name='user', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(blank=True, verbose_name='user permissions', to='auth.Permission', help_text='Specific permissions for this user.', related_query_name='user', related_name='user_set')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
