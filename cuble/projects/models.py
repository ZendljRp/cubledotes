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
from core.models import AbstractArticle
from tags.models import Tag


class Project(AbstractArticle):
    """
    Post for blogging.
    """
    description = models.TextField(null=True)
    tags = models.ManyToManyField(Tag, related_name="projects")

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        @param args:
        @param kwargs:
        """
        slug_base = self.slug if self.slug else self.title
        self.slug = slugify(slug_base)
        super(Project, self).save(*args, **kwargs)
