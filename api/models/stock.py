# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from rest_framework import serializers

from api.models.product_variant import Product_variant
from api.models.store import Store


class Stock(models.Model):

    MOVE_TYPES = (('moved_to_store','Moved to store'),('non_saleable','Marked as non-saleable'),)

    created                  = models.DateTimeField(auto_now_add=True, blank=False)
    updated                  = models.DateTimeField(auto_now_add=True, blank=True)

    store                    = models.ForeignKey(Store, blank=False, null=False)
    product_variant          = models.ForeignKey(Product_variant, blank=False, null=False)
    quantity                 = models.DecimalField(default=0, max_digits=10, decimal_places=0, blank=True, null=True)

    def __unicode__(self):
        return '%s %s %s %s' % (self.id, self.store, self.product_variant, self.quantity)

    class Meta:
        ordering            = ('created',)
        app_label           = 'api'
        verbose_name        = 'Stock'
        verbose_name_plural = 'Stocks'


class Stock_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = (
                    'created',
                    'updated',
                    'store',
                    'product_variant',
                    'quantity'
                 )
