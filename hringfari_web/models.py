# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from django.core.urlresolvers import reverse

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class Category(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length = 250)
    slug = models.SlugField()
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __unicode__(self):
        return u"%d %s" % (self.order, self.name)
        
    def all_content(self):
        return [link.content for link in  CategoryToContent.objects.filter(category = self)]
    
class Content(models.Model):
    name = models.CharField(max_length = 250)
    slug = models.SlugField()
    
    html_file = models.CharField(max_length = 250)
    
    def __unicode__(self):
        return u"%s -> %s" % (self.name, self.html_file)
        
    def get_absolute_url(self):
        return reverse("show_content", kwargs = {'content_slug': self.slug })
    
class CategoryToContent(models.Model):
    category = models.ForeignKey(Category)
    content = models.ForeignKey(Content)
    
    def __unicode__(self):
        return u"%s >> %s" % (self.category, self.content.name)
    
    
