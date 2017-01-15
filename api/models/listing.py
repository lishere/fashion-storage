# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from rest_framework import serializers

from api.models.product_move import Product_move
from api.models.product_variant import Product_variant
# from api.models.product_variant_quantity import Product_variant_quantity


class Listing(models.Model):

    MOVE_TYPES = (('moved_to_store','Moved to store'),('non_saleable','Marked as non-saleable'),)

    created                  = models.DateTimeField(auto_now_add=True, blank=False)
    updated                  = models.DateTimeField(auto_now_add=True, blank=True)

    #sale_id                 = models.ForeignKey(Sale, blank=True)
    product_move_id          = models.ForeignKey(Product_move, blank=True)
    # product_variant_quantity = models.ForeignKey(Product_variant_quantity, blank=False)
    product_variant         = models.ForeignKey(Product_variant, blank=False)
    quantity                = models.DecimalField(default=0, max_digits=10, decimal_places=0, blank=False)

    def __unicode__(self):
        return '%s %s' % (self.id, self.product_move_id)

    class Meta:
        ordering            = ('created',)
        app_label           = 'api'
        verbose_name        = 'Listing'
        verbose_name_plural = 'Listings'


class Listing_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = (
                    'created',
                    'updated',
                    'product_move_id'
                 )
