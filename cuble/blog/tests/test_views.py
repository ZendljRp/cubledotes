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
from blog.models import Post


class BlogViewTests(TestCase):
    def setUp(self):
        self.user_password = "pass"
        self.user = mommy.make('profiles.User', email='user@example.com')
        self.user.set_password(self.user_password)
        self.user.save()

    def test_blog(self):
        mommy.make('blog.Post', author=self.user, _quantity=5)
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)

    def test_blog_tags(self):
        tag = mommy.make('tags.Tag')
        mommy.make('blog.Post', author=self.user, tags=[tag], _quantity=5)
        response = self.client.get(reverse('posts_tag', kwargs={'slug': tag.slug}))
        self.assertEqual(response.status_code, 200)

    def test_blog_feed(self):
        mommy.make('blog.Post', author=self.user, _quantity=5)
        response = self.client.get(reverse('blog_feed'))
        self.assertEqual(response.status_code, 200)

    def test_blog_atom(self):
        mommy.make('blog.Post', author=self.user, _quantity=5)
        response = self.client.get(reverse('blog_atom'))
        self.assertEqual(response.status_code, 200)

    def test_blog_details(self):
        post = Post.objects.create(author=self.user, title="Title", slug="slug", status=Post.PUBLISHED)
        response = self.client.get(reverse('post', kwargs={'slug': post.slug}))
        self.assertEqual(response.status_code, 200)
