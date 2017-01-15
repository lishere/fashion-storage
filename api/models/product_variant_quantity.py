# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import serializers

from api.models.product_variant import Product_variant
from api.models.listing import Listing


class Product_variant_quantity(models.Model):

    created                 = models.DateTimeField(auto_now_add=True, blank=False)
    updated                 = models.DateTimeField(auto_now_add=True, blank=True)

    #listing                 = models.ForeignKey(Listing, blank=False)
    #product_variant         = models.ForeignKey(Product_variant, blank=False)
    #quantity                = models.DecimalField(default=0, max_digits=10, decimal_places=0, blank=False)

    #def __unicode__(self):
        #return '%s %s %s' % (self.created, self.product_variant, self.quantity)

    class Meta:
        ordering            = ('id',)
        app_label           = 'api'
        verbose_name        = 'Product variant quantity'
        verbose_name_plural = 'Product variant quantities'


class Product_variant_quantity_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product_variant_quantity
        fields = (
                    'created',
                    'updated',
                    'product_variant',
                    'quantity'
                 )
