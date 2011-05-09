# -*- coding: utf-8 -*-
import os.path

from django import template
register = template.Library()

from hringfari_web.models import Content, Category

def list_of_categories(context):
    request = context.get("request")
    content_slug = None
    if request is not None:
        head, content_slug = os.path.split(request.path[:-1])
        
    categories = Category.objects.all().order_by("order")
        
    return {'categories': categories, 'open_content_slug': content_slug }
        
register.inclusion_tag('list_of_content.html', takes_context=True)(list_of_categories)