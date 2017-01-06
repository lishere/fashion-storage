
# -*- coding: utf-8 -*-

from django.db import models
#from django.contrib.contenttypes import *

class Note(models.Model):
    created             = models.DateTimeField(auto_now_add=True, blank=False)
    #attached_to         = models.GenericForeignKey('content_type', 'object_id')
    body                = models.TextField(blank=False)
    # user

    class Meta:
        ordering    = ('created',)
        app_label   = 'api'
