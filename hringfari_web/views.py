# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404

from hringfari_web.models import Content

def index(request):
    
    return render_to_response("base.html", {})
    
    
def show_content(request, content_slug):
    content = get_object_or_404(Content, slug = content_slug)
    
    return render_to_response("content/%s" % content.html_file, {})