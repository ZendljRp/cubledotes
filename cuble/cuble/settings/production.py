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
from cuble.settings.base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION

########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = [
    'cuble.pythonanywhere.com',
    '.cuble.es',
]
########## END HOST CONFIGURATION

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_USE_TLS = True
EMAIL_HOST = get_env_setting('EMAIL_HOST')
EMAIL_HOST_USER = get_env_setting('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_setting('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env_setting('DB_NAME'),
        'USER': get_env_setting('DB_USER'),
        'PASSWORD': get_env_setting('DB_PASSWORD'),
        'HOST': get_env_setting('DB_HOST'),
        'PORT': get_env_setting('DB_PORT'),
    }
}
########## END DATABASE CONFIGURATION

########## EASY THUMBNAILS CONFIGURATION
# THUMBNAIL_DEFAULT_STORAGE = "storages.backends.s3boto.S3BotoStorage"
########## END EASY THUMBNAILS CONFIGURATION

########### STORAGES CONFIGURATION
# AWS_ACCESS_KEY_ID = get_env_setting('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = get_env_setting('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = get_env_setting('AWS_STORAGE_BUCKET_NAME')
# AWS_QUERYSTRING_AUTH = False
# DEFAULT_FILE_STORAGE = 'core.s3utils.MediaRootS3BotoStorage'
# MEDIA_URL = "//{}.s3.amazonaws.com/media/".format(AWS_STORAGE_BUCKET_NAME)
# STATICFILES_STORAGE = 'core.s3utils.StaticRootS3BotoStorage'
# STATIC_URL = "//{}.s3.amazonaws.com/static/".format(AWS_STORAGE_BUCKET_NAME)
########### END STORAGES CONFIGURATION

########## SOUTH CONFIGURATION
# SOUTH_DATABASE_ADAPTERS = {
#     'default': 'south.db.mysql'
# }
########## END SOUTH CONFIGURATION
