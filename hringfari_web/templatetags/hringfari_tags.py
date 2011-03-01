# -*- coding: utf-8 -*-

from django import template
register = template.Library()


def list_of_content(context):
    request = context.get("request")
        
        
    return {}
        
register.inclusion_tag('list_of_content.html', takes_context=True)(list_of_content)