# -*- coding: utf-8 -*-
from django.db import models

class Content(models.Model):
    name = models.CharField(max_length = 250)
    slug = models.SlugField()
    
    html_file = models.CharField(max_length = 250)
    
    
