
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Note(models.Model):
    created             = models.DateTimeField(auto_now_add=True, blank=False)
    content_type        = models.ForeignKey(ContentType, default=0)
    object_id           = models.PositiveIntegerField(default=0)
    attached_to         = GenericForeignKey('content_type', 'object_id')
    body                = models.TextField(blank=False)
    # user

    class Meta:
        ordering    = ('created',)
        app_label   = 'api'
