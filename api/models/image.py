# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import serializers

from api.models.product import Product

class Image(models.Model):

    PERSPECTIVES    = (('front','Front'),('side','Side'),('back','Back'),('detail','Detail'),)

    created         = models.DateTimeField(auto_now_add=True, blank=False)
    updated         = models.DateTimeField(auto_now_add=True, blank=True)
    is_active       = models.BooleanField(default=True, blank=True)

    product         = models.ForeignKey(Product, default=1, blank=False)
    color_1_en      = models.CharField(max_length=50, blank=False, verbose_name='Main color in English')
    color_2_en      = models.CharField(max_length=50, blank=True, verbose_name='Second color in English')
    image           = models.ImageField(upload_to='images', blank=True)
    perspective     = models.CharField(max_length=10, choices=PERSPECTIVES, blank=True)
    photographer    = models.CharField(max_length=50, blank=True)
    year            = models.SmallIntegerField(blank=True, help_text='When was this photo taken?')

    def __unicode__(self):
        return '%s %s %s %s %s %s' % ( self.product, self.color_1_en.title(), self.color_2_en.title(), self.perspective.title(), self.photographer, self.year)

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
                    'product',
                    'color_1_en',
                    'color_2_en',
                    'image',
                    'perspective',
                    'photographer',
                    'year'
                   )
