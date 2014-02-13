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
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.db import models
from filer.fields.file import FilerFileField
from core.managers import ArticlesManager


class AbstractArticle(models.Model):
    """
    Abstract model for articles, posts, projects, etc.
    """
    DRAFT, SCHEDULED, PUBLISHED = (0, 1, 2)
    STATUSES = (
        (DRAFT, _("Draft")),
        (SCHEDULED, _("Scheduled")),
        (PUBLISHED, _("Published")),
    )

    status = models.PositiveIntegerField(choices=STATUSES, default=DRAFT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.TextField()
    slug = models.SlugField(blank=True, unique=True)
    content = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now())
    scheduled_at = models.DateTimeField(null=True, blank=True)

    outstanding_image = FilerFileField(null=True, blank=True)

    objects = ArticlesManager()

    class Meta:
        abstract = True
