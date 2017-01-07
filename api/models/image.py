# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import serializers


class Image(models.Model):

    PERSPECTIVES    = (('front','Front'),('side','Side'),('back','Back'),('detail','Detail'),)

    created         = models.DateTimeField(auto_now_add=True, blank=False)
    updated         = models.DateTimeField(auto_now_add=True, blank=True)
    is_active       = models.BooleanField(default=True, blank=True)

    image           = models.ImageField(upload_to='images', blank=True)
    perspective     = models.CharField(max_length=10, choices=PERSPECTIVES, blank=True)
    photographer    = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return '%s %s' % (self.given_name, self.surname)

    class Meta:
        ordering            = ('created',)
        app_label           = 'api'
        verbose_name        = 'Image'
        verbose_name_plural = 'Images'


class Image_serializer(serializers.HyperlinkedModelSerializer):

    def __unicode__(self):
        return self.id

    class Meta:
        model   = Image
        fields  = (
                    'is_active',
                    'created',
                    'updated',
                    'image',
                    'perspective',
                    'photographer'
                   )
