# -*- coding: utf-8 -*-

from django.db import models
from django.utils.text import Truncator
from django.contrib.contenttypes.fields import GenericForeignKey
from rest_framework import serializers

from django.contrib.contenttypes.models import ContentType


class Note(models.Model):
    created             = models.DateTimeField(auto_now_add=True, blank=False)
    content_type        = models.ForeignKey(ContentType, default=0)
    object_id           = models.PositiveIntegerField(default=0)
    attached_to         = GenericForeignKey('content_type', 'object_id')
    body                = models.TextField(blank=False)
    # user

    def __unicode__(self):
        return Truncator(self.body).chars(40)

    class Meta:
        ordering    = ('-created',)
        app_label   = 'api'
        verbose_name = 'Internal note'
        verbose_name_plural = 'Internal notes'


class Note_serializer(serializers.HyperlinkedModelSerializer):

    def __unicode__(self):
        return self.id

    class Meta:
        model = Note
        fields = ('created',
                  'body')
