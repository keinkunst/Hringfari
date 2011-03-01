# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

#handler404 = 'dexweb.views.not_found'
#handler500 = 'dexweb.views.server_error'

from hringfari_web.views import index
from hringfari_web.views import content_index, show_content

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', index),
    url('^verkefni/$', content_index),
    url('^verkefni/(?P<content_slug>[^/]+)/$', show_content)
)

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/dexoris/django_projects/dexoris/media/'}),
    )
