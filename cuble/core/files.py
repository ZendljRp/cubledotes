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
import hashlib
import time
import random
import os
from django.utils.text import slugify


def name_to_path(path):
    """ Generates a function to give  to ``upload_to`` parameter in
    models.Fields, that generates an unique name for uploaded files. """

    def name(instance, filename):
        """  Generates an unique name for an uploaded file. """
        ext = filename.split('.')[-1]
        name_to_hash = "{}--{}".format(time.time(), random.random())
        file_name = hashlib.sha256(name_to_hash.encode('utf-8'))
        file_format = "{}.{}".format(file_name.hexdigest(), ext)
        return os.path.join(path, file_format)
    return name


def readable_name_to_path(path, populate_from=None):
    """
    Generates a function to give  to ``upload_to`` parameter in
    models.Fields, that generates an name for uploaded files based on ``populate_from``
    attribute.
    """

    def name(instance, filename):
        """
        Generates an name for an uploaded file.
        """
        if populate_from is not None and not hasattr(instance, populate_from):
            raise AttributeError("Instance hasn't {} attribute".format(populate_from))
        ext = filename.split('.')[-1]
        readable_name = slugify(filename.split('.')[0])
        if populate_from:
            readable_name = slugify(getattr(instance, populate_from))
        file_name = "{}.{}".format(readable_name, ext)
        return os.path.join(path, file_name)
    return name
