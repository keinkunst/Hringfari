# -*- coding: utf-8 -*-

from django.contrib import admin

from hringfari_web.models import Content
from hringfari_web.models import Category
from hringfari_web.models import CategoryToContent

admin.site.register(Content)
admin.site.register(Category)
admin.site.register(CategoryToContent)