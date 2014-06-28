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
from django.test import TestCase

from model_mommy import mommy

from projects.forms import BudgetForm
from projects.models import Budget


class FormsTests(TestCase):
    def setUp(self):
        self.user_password = "pass"
        self.user = mommy.make('profiles.User', email='user@example.com')
        self.user.set_password(self.user_password)
        self.user.save()

    def test_new_budget_form(self):
        prev_budgets = Budget.objects.all().count()
        data = {
            "name": "Test project",
            "email": "test@example.com",
            "title": "title",
            "stage": Budget.NEW_PROJECT,
            "type": Budget.TYPE_WEB,
            "about": "About",
            "hosting_type": Budget.DONT_KNOW,
            "web_design_stage": Budget.NEW_DESIGN,
            "badget": "2000-4000",
        }
        form = BudgetForm(data)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(Budget.objects.all().count(), prev_budgets + 1)
