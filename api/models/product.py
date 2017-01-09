# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import serializers


class Product(models.Model):

    PRODUCT_TYPES   = (('coat','Coat'),('dress','Dress'),('jacket','Jacket'),('longsleeve','Longsleeve'),('pullover','Pullover'),('shirt','Shirt'),('skirt','Skirt'),('trousers','Trousers'),('other','Other'))
    GENDER          = (('women','Women'),('men','Men'),('unisex','unisex'),)

    created             = models.DateTimeField(auto_now_add=True, blank=False)
    updated             = models.DateTimeField(auto_now_add=True, blank=True)
    is_active           = models.BooleanField(default=True, blank=True)

    name                = models.CharField(max_length=50, blank=False)
    type                = models.CharField(max_length=50, choices=PRODUCT_TYPES, blank=False)
    target_group        = models.CharField(max_length=6, default='unisex', choices=GENDER, blank=False)
    description_de      = models.TextField(max_length=500, blank=True, verbose_name='German description')
    description_en      = models.TextField(max_length=500, blank=True, verbose_name='English description')
    description_it      = models.TextField(max_length=500, blank=True, verbose_name='Italian description')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering            = ('-name',)
        app_label           = 'api'
        verbose_name        = 'Product'
        verbose_name_plural = 'Products'


class Product_serializer(serializers.HyperlinkedModelSerializer):

    def __unicode__(self):
        return self.id

    class Meta:
        model = Product
        fields = (
                  'created',
                  'updated',
                  'is_active',
                  'name',
                  'type',
                  'target_group',
                  'description_de',
                  'description_en',
                  'description_it'
                 )
