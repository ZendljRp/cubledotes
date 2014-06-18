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
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from blog.models import Post, Tag
from projects.models import Project


class ProjectsListView(View):
    """
    List of posts.
    """

    @staticmethod
    def get(request):
        """

        @param request:
        @return:
        """
        projects = Project.objects.requested_objects(request)
        return render(request, "projects/list.html", {"projects": projects})


class ProjectsTagListView(View):
    """
    List of posts.
    """

    @staticmethod
    def get(request, slug):
        """

        @param request:
        @return:
        """
        tag = get_object_or_404(Tag, slug=slug)
        projects = Project.objects.requested_objects(request, queryset=tag.projects.all())
        return render(request, "projects/list.html", {"projects": projects, "tag": tag})


class ProjectDetailsView(View):
    """
    List of posts.
    """

    @staticmethod
    def get(request, slug):
        """

        @param request:
        @param slug:
        @return:
        """
        project = get_object_or_404(Project, slug=slug)
        return render(request, "projects/details.html", {"project": project})