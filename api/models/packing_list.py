# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from rest_framework import serializers

from api.models.product_move import Product_move


class Packing_list(models.Model):

    created                 = models.DateTimeField(auto_now_add=True, blank=False)
    updated                 = models.DateTimeField(auto_now_add=True, blank=True)
    is_active               = models.BooleanField(default=True, blank=True)

    date                    = models.DateTimeField(default=datetime.now, blank=False)
    correction_for          = models.ForeignKey("self", related_name="selfref", blank=True, null=True)
    product_move            = models.ForeignKey(Product_move, related_name="productmoveref", blank=True, null=True)

    def __unicode__(self):
        return '%s %s %s' % (self.date, self.id, self.product_move)

    class Meta:
        ordering            = ('date',)
        app_label           = 'api'
        verbose_name        = 'Packing list'
        verbose_name_plural = 'Packing lists'


class Packing_list_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Packing_list
        fields = (
                    'created',
                    'updated',
                    'date',
                    'correction_for',
                    'product_move',
                 )
