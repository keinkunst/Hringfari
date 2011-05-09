# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext

from hringfari_web.models import Content

def index(request):
    
    return render_to_response("base.html", {}, context_instance = RequestContext(request))  
    
def content_index(request):
    
    return render_to_response("content.html", {}, context_instance = RequestContext(request))  
    
def help(request):
    return render_to_response("help.html", {}, context_instance = RequestContext(request))    
    
def show_content(request, content_slug):
    content = get_object_or_404(Content, slug = content_slug)
    
    return render_to_response("content/%s" % content.html_file, {'content': content }, context_instance = RequestContext(request)) 