# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import serializers


class Packing_list(models.Model):

    created             = models.DateTimeField(auto_now_add=True, blank=False)
    updated             = models.DateTimeField(auto_now_add=True, blank=True)
    

    def __unicode__(self):
        return self.get_name_display()

    class Meta:
        ordering            = ('name',)
        app_label           = 'api'
        verbose_name        = 'Packing_list'
        verbose_name_plural = 'Countries'


class Packing_list_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Packing_list
        fields = (
                    'created',
                    'updated',
                    'name',
                    'vat_rate',
                    'category',
                    'currency'
                 )
