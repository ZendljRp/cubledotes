# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2014

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
from crispy_forms.layout import Layout, Fieldset

from django.forms import ModelForm
from django.utils.translation import ugettext as _

import floppyforms
from crispy_forms.helper import FormHelper

from projects.models import Budget


class BudgetForm(ModelForm):
    """
    Form for create budgets.
    """

    class Meta:
        model = Budget
        widgets = {
            "stage": floppyforms.widgets.RadioSelect(),
            "type": floppyforms.widgets.RadioSelect(),
            "hosting": floppyforms.widgets.RadioSelect(
                choices=((True, _("Sí")), (False, _("No")))
            ),
            "hosting_assistance": floppyforms.widgets.RadioSelect(
                choices=((True, _("Sí")), (False, _("No")))
            ),
            "hosting_type": floppyforms.widgets.RadioSelect(),
            "hosting_quotes": floppyforms.widgets.Select(),
            "web_design_stage": floppyforms.widgets.RadioSelect(),
            "branding_design": floppyforms.widgets.RadioSelect(
                choices=((True, _("Sí")), (False, _("No")))
            ),
            "web_design": floppyforms.widgets.RadioSelect(
                choices=((True, _("Sí")), (False, _("No")))
            ),
            "responsive_web_design": floppyforms.widgets.RadioSelect(
                choices=((True, _("Sí")), (False, _("No")))
            ),
            "badget": floppyforms.widgets.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super(BudgetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('<span>&gt; 1</span> Información personal'),
                'name',
                'email',
                'company',
            ),
            Fieldset(
                _('<span>&gt; 2</span> Información general del proyecto'),
                'title',
                'stage',
                'type',
                'other_type',
                'about',
            ),
            Fieldset(
                _('<span>&gt; 3</span> Hosting del proyecto'),
                'hosting',
                'hosting_assistance',
                'hosting_type',
                'hosting_quotes',
            ),
            Fieldset(
                _('<span>&gt; 4</span> Diseño'),
                'branding_design',
                'branding_design_about',
                'web_design',
                'web_design_stage',
                'responsive_web_design',
                'responsive_web_design',
            ),
            Fieldset(
                _('<span>&gt; 5</span> Presupuesto'),
                'badget',
                'badget_file',
            )
        )