# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from rest_framework import serializers

from api.models.product_move import Product_move
from api.models.product_variant import Product_variant


class Listing(models.Model):

    created                  = models.DateTimeField(auto_now_add=True, blank=False)
    updated                  = models.DateTimeField(auto_now_add=True, blank=True)

    product_move_id          = models.ForeignKey(Product_move, blank=True, null=True)

    product_variant          = models.ForeignKey(Product_variant, blank=True, null=True)
    quantity                 = models.DecimalField(default=0, max_digits=10, decimal_places=0, blank=True, null=True)
    is_destroyed             = models.BooleanField(default=False, blank=True, verbose_name="Destroyed?", help_text="Mark products(s) as destroyed, stolen or otherwise non-saleable")

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
