# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2014 Cuble Desarrollo S.L.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext as _
from easy_thumbnails.fields import ThumbnailerImageField

from core.files import readable_name_to_path
from core.models import AbstractArticle
from tags.models import Tag


class Project(AbstractArticle):
    """
    Post for blogging.
    """
    description = models.TextField(null=True)
    tags = models.ManyToManyField(Tag, related_name="projects")

    thumbnail_image = ThumbnailerImageField(upload_to=readable_name_to_path('images'), null=True, blank=True)

    def __unicode__(self):
        return self.title

    def thumbnail(self):
        """
        @return:
        """
        if self.thumbnail_image is None:
            return self.outstanding_image
        return self.thumbnail_image

    def save(self, *args, **kwargs):
        """
        @param args:
        @param kwargs:
        """
        slug_base = self.slug if self.slug else self.title
        self.slug = slugify(slug_base)
        super(Project, self).save(*args, **kwargs)


class Budget(models.Model):
    """
    Model por a budget proposal.
    """
    NEW_PROJECT, EXISTING_PROJECT = (0, 1)
    STAGE_CHOICES = (
        (NEW_PROJECT, _("Nuevo Proyecto")),
        (EXISTING_PROJECT, _("Retomar Proyecto")),
    )

    TYPE_ECOMMERCE, TYPE_WEB, TYPE_BACKEND, TYPE_SERVERS, TYPE_OTHER = (0, 1, 2, 3, 5)
    PROJECT_TYPE_CHOICES = (
        (TYPE_ECOMMERCE, _("Comercio Electrónico")),
        (TYPE_WEB, _("Plataforma Web")),
        (TYPE_BACKEND, _("Backend App")),
        (TYPE_SERVERS, _("Gestión Servidores")),
        (TYPE_OTHER, _("Otro")),
    )

    AWS, RACKSPACE, OTHER, DONT_KNOW = (0, 1, 2, 3)
    HOSTING_CHOICES = (
        (AWS, _("Amazon Web Services")),
        (RACKSPACE, _("Rackspace")),
        (OTHER, _("Otro")),
        (DONT_KNOW, _("No lo se")),
    )

    HOSTING_QUOTES_CHOICES = (
        ("100", _("100")),
        ("200", _("200")),
        ("300", _("300")),
        ("Más de 300", _("Más de 300")),
    )

    NEW_DESIGN, REDISEGN = (0, 1)
    DESIGN_STAGE_CHOICES = (
        (NEW_DESIGN, _("Nuevo")),
        (REDISEGN, _("Rediseño")),
    )

    BADGET_QUOTES_CHOICES = (
        ("2000-4000", _("2.000 - 4.000")),
        ("4000-6000", _("4.000 - 6.000")),
        ("6000-8000", _("6.000 - 8.000")),
        ("Más de 8000", _("Más de 8.000")),
    )

    name = models.CharField(max_length=128)
    email = models.EmailField()
    company = models.CharField(verbose_name=_("Empresa"), max_length=128, null=True, blank=True)

    title = models.CharField(verbose_name=_("Nombre del proyecto"), max_length=128)
    stage = models.IntegerField(
        verbose_name=_("Etapa del proyecto"),
        choices=STAGE_CHOICES,
        default=NEW_PROJECT
    )
    type = models.IntegerField(
        verbose_name=_("Tipo de proyecto"),
        choices=PROJECT_TYPE_CHOICES,
        default=TYPE_WEB
    )
    other_type = models.CharField(
        verbose_name=_("En caso de ser otro tipo de proyecto, especifica cual"),
        max_length=128,
        null=True,
        blank=True
    )
    about = models.TextField(
        verbose_name=_("Acerca del proyecto (en que consiste, a quién va dirigido, etc.)"),
    )

    hosting = models.BooleanField(verbose_name=_("¿Ya tienes hosting?"), default=False)
    hosting_assistance = models.BooleanField(verbose_name=_("¿Necesitas asesoramiento para contratar el hosting?"),
                                             default=False)
    hosting_type = models.IntegerField(
        verbose_name=_("¿Que hosting quieres contratar?"),
        choices=HOSTING_CHOICES,
        default=DONT_KNOW,
        blank=True
    )
    hosting_quotes = models.CharField(
        verbose_name=_("¿Cuál es tu presupuesto mensual para el hosting?"),
        max_length=128,
        choices=HOSTING_QUOTES_CHOICES,
        null=True,
        blank=True
    )

    branding_design = models.BooleanField(
        verbose_name=_("¿Necesitas que diseñemos tu identidad corporativa?"),
        default=True
    )
    branding_design_about = models.TextField(
        verbose_name=_("Hablanos un poco sobre el diseño de identidad que quieres para el proyecto"),
        default="",
        blank=True,
    )
    web_design = models.BooleanField(
        verbose_name=_("¿Necesitas que diseñemos tu sitio web?"),
        default=True
    )
    web_design_stage = models.IntegerField(
        verbose_name=_("Etapa del diseño"),
        choices=DESIGN_STAGE_CHOICES,
        default=NEW_DESIGN,
        blank=True
    )
    responsive_web_design = models.NullBooleanField(
        verbose_name=_("¿Necesitas diseño responsive para tu sitio web?"),
        null=True,
        blank=True
    )

    badget = models.CharField(
        verbose_name=_("¿Qué presupuesto tienes disponible para el proyecto?"),
        max_length=128,
        choices=BADGET_QUOTES_CHOICES
    )
    badget_file = models.FileField(
        verbose_name=_("Si dispones de un briefing del proyecto no dudes en enviárlo"),
        upload_to=readable_name_to_path('badgets'),
        null=True,
        blank=True
    )