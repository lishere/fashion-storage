# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import serializers

from api.models.store import Store
from api.models.product_variant import Product_variant
from api.models.store import Store


class Product_variant_price_per_store(models.Model):

    created                 = models.DateTimeField(auto_now_add=True, blank=False)
    updated                 = models.DateTimeField(auto_now_add=True, blank=True)

    rec_gross_sale_price    = models.DecimalField(default=0, max_digits=6, decimal_places=2, blank=False, verbose_name='Recommended gross sale price in this store and in the currency of the stores country')
    product_variant         = models.ForeignKey(Product_variant, blank=False)
    store                   = models.ForeignKey(Store, blank=False)

    def __unicode__(self):
        return '%s %s %s' % (self.product_variant, self.store, self.rec_gross_sale_price)

    class Meta:
        ordering            = ('id',)
        app_label           = 'api'
        verbose_name        = 'Product variant price per store'
        verbose_name_plural = 'Product variant prices per store'


class Product_variant_price_per_store_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product_variant_price_per_store
        fields = (
                    'created',
                    'updated',
                    'product_variant',
                    'rec_gross_sale_price',
                    'store'
                 )
