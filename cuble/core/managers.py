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
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models


class ArticlesManager(models.Manager):
    """
    Manager for posts.
    """

    def requested_objects(self, request, page=None, queryset=None):
        """
        @param queryset:
        @param request:
        @param page:
        @return:
        """
        if not queryset:
            queryset = self.all()
        posts_list = queryset.filter(status=self.model.PUBLISHED).order_by('-created_at')
        paginator = Paginator(posts_list, 5)  # TODO Parametrizar
        if page is None:
            page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return posts