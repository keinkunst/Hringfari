# -*- coding: utf-8 -*-
import os.path

from django.conf import settings
from django.db.models.signals import post_syncdb

import hringfari_web.models as models
from hringfari_web.models import Content


def sync_with_content_folder(sender, app, created_models, verbosity, interactive, **kwargs):
    if sender == models:
        content_directory = u"hringfari_web/templates/content"
        for dirname, dirnames, filenames in os.walk(content_directory):
            for filename in filenames:
                if filename.endswith(u".html"):      
                    try:
                        content = Content.objects.get(html_file = filename)
                    except Content.DoesNotExist:
                        name = filename.replace(".html", "")
                        content = Content.objects.create(name = name.title(),
                                                         slug = name,
                                                         html_file = filename)
                                                         
                        print u"Creating content ", filename
                                                                        
                    
post_syncdb.connect(sync_with_content_folder)