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

from django.test import TestCase
from django.utils.text import slugify
from model_mommy import mommy

from blog.models import Post


class PostModelTests(TestCase):

    def setUp(self):
        self.user_password = "pass"
        self.user = mommy.make('profiles.User', email='user@example.com')
        self.user.set_password(self.user_password)
        self.user.save()

    def _create_post(self, content="foo"):
        return Post.objects.create(
            author=self.user,
            content=content,
            title="Title",
            slug="Title"
        )

    def test_create_post(self):
        prev_posts = Post.objects.count()
        self._create_post()
        self.assertEqual(prev_posts + 1, Post.objects.count())

    def test_create_slug(self):
        post = mommy.make('blog.Post', author=self.user)
        post.save()
        self.assertEqual(post.slug, slugify(post.title))

    def test_more(self):
        original_summary = "part1"
        post = self._create_post("{}<!--more-->more".format(original_summary))
        summary = post.summary()
        self.assertEqual(summary, '{}<p><a href="/blog/title/">Seguir leyendo...</a></p>'.format(original_summary))