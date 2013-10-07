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
from .base import *

########## TEST SETTINGS
TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = SITE_ROOT
TEST_DISCOVER_ROOT = SITE_ROOT
TEST_DISCOVER_PATTERN = "test_*.py"
########## END TEST SETTINGS


########## DATABASE CONFIGURATION
# In-memory configuration
DATABASES = {
                "default": {
                    "ENGINE": "django.db.backends.sqlite3",
                    "NAME": ":memory:",
                    "USER": "",
                    "PASSWORD": "",
                    "HOST": "",
                    "PORT": "",
                },
             }
########## END DATABASE CONFIGURATION


########## AMAZON AWS CONFIGURATION
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
########## END AMAZON AWS CONFIGURATION

########## MOMMY CONFIGURATION
import random
MOMMY_CUSTOM_FIELDS_GEN = {
    'core.fields.LocationField': lambda: u"%s;%s" % (random.random()*100, random.random()*100),
}
########## END MOMMY CONFIGURATION