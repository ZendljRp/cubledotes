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
from django.core.urlresolvers import reverse
from django.test import TestCase
from model_mommy import mommy


class PagesViewTests(TestCase):
    def setUp(self):
        self.user_password = "pass"
        self.user = mommy.make('profiles.User', email='user@example.com')
        self.user.set_password(self.user_password)
        self.user.save()

    def _authenticate(self):
        self.client.login(
            email='user@example.com',
            password=self.user_password,
            is_validate=True,
        )

    def test_landing(self):
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)

    def test_services(self):
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
