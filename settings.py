# -*- coding: utf-8 -*-
# Django settings for dexoris project.

from djangoappengine.settings_base import *
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    (u'Kristján Einarsson', "einarsson.kr@gmail.com"),
    (u'Jóhann Þ. Bergþórsson', 'johann.thorvaldur@gmail.com'),
)

MANAGERS = ADMINS

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+)o79h289rlj^2y7!ar^hnqvy+-x$ry)8xo-c3wfbyi#j@y-f2'

INSTALLED_APPS = (
    'djangoappengine',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'djangotoolbox',
    
    'hringfari_web',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
STATICFILES_ROOT = os.path.join(os.path.dirname(__file__), '_generated_media')
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static'),
)
STATICFILES_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'

SITE_ID = 1

try:
    import dbindexer
    DATABASES['native'] = DATABASES['default']
    DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
    INSTALLED_APPS += ('dbindexer',)
except ImportError:
    pass
