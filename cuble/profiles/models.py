# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2013 Cuble Desarrollo S.L.

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
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Cuble user.
    """
    bio = models.TextField(_("Description"), null=True, blank=True)

    # SKILLS
    MAX_SKILL = 7

    DEVELOPERS_SKILLS_FIELDS = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
    DESIGNER_SKILLS_FIELDS = []
    MANAGER_SKILLS_FIELDS = []

    strength = models.PositiveIntegerField(verbose_name=_('Strength'), help_text=_("Programming Python/Django"), default=1)
    dexterity = models.PositiveIntegerField(verbose_name=_('Dexterity'), help_text=_("Programming Javascript/HTML5/CSS3"), default=1)
    constitution = models.PositiveIntegerField(verbose_name=_('Constitution'), help_text=_("Server Architecture"), default=1)
    intelligence = models.PositiveIntegerField(verbose_name=_('Intelligence'), help_text=_("Software Design and Theory"), default=1)
    wisdom = models.PositiveIntegerField(verbose_name=_('Wisdom'), help_text=_("Data Bases"), default=1)
    charisma = models.PositiveIntegerField(verbose_name=_('Charisma'), help_text=_("Management"), default=1)

    def skills(self):
        """

        :return:
        """
        skills = list()
        fields = self.DEVELOPERS_SKILLS_FIELDS
        for field_name in fields:
            skills.append(
                (
                    self._meta.get_field_by_name(field_name)[0].verbose_name,
                    self._meta.get_field_by_name(field_name)[0].help_text,
                    getattr(self, field_name) / self.MAX_SKILL * 100.0,
                    getattr(self, field_name)
                )
            )
        return skills


class Link(models.Model):
    """
    Generic links for users.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='links')
    url = models.URLField()
    icon = models.CharField(max_length=128)
    title = models.CharField(max_length=128, null=True, blank=True)