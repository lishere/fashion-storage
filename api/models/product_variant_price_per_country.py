# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import serializers

from api.models.country import Country
from api.models.product_variant import Product_variant


class Product_variant_price_per_country(models.Model):

    created                 = models.DateTimeField(auto_now_add=True, blank=False)
    updated                 = models.DateTimeField(auto_now_add=True, blank=True)

    rec_gross_sale_price    = models.DecimalField(default=0, max_digits=6, decimal_places=2, blank=False, verbose_name='Recommended gross sale price in the currency of the country')
    product_variant         = models.ForeignKey(Product_variant, blank=False)
    country                 = models.ForeignKey(Country, blank=False)

    def __unicode__(self):
        return '%s %s %s' % (self.product_variant, self.country.get_name_display(), self.rec_gross_sale_price)

    class Meta:
        ordering            = ('id',)
        app_label           = 'api'
        verbose_name        = 'Product variant price per country'
        verbose_name_plural = 'Product variant prices per country'


class Product_variant_price_per_country_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product_variant_price_per_country
        fields = (
                    'created',
                    'updated',
                    'product_variant',
                    'rec_gross_sale_price',
                    'country'
                 )
