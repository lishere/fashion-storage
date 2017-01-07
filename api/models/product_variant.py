# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import serializers


class Product_variant(models.Model):

    SIZES = (('s','S'),('xs','XS'),('m','M'),('l','L'),('xl','XL'),('xxl','XXL'),('ws','Women S'),('wxs','Women XS'),('wm','Women M'),('wl','Women L'),('wxl','Women XL'),('ms','Men S'),('mxs','Men XS'),('mm','Men M'),('ml','Men L'),('mxl','Men XL'),('mxxl','Men XXL'),)

    created                         = models.DateTimeField(auto_now_add=True, blank=False)
    updated                         = models.DateTimeField(auto_now_add=True, blank=True)
    is_active                       = models.BooleanField(default=True, blank=True)
    is_organic                      = models.BooleanField(default=False, blank=False, verbose_name="Organic")

    # product
    # images

    rec_gross_sale_price_default    = models.DecimalField(max_digits=6, decimal_places=2, blank=True, verbose_name='Recommended default gross sale price')
    # rec_gross_sale_price_by_country
    size                            = models.CharField(max_length=6, default='m', choices=SIZES, blank=True)

    name_en                         = models.CharField(max_length=50, blank=False, verbose_name='English name')
    name_de                         = models.CharField(max_length=50, blank=True, verbose_name='German name')
    name_it                         = models.CharField(max_length=50, blank=True, verbose_name='Italian name')
    description_de                  = models.TextField(max_length=500, blank=True, verbose_name='German description')
    description_en                  = models.TextField(max_length=500, blank=True, verbose_name='English description')
    description_it                  = models.TextField(max_length=500, blank=True, verbose_name='Italian description')
    care_instructions_de            = models.TextField(max_length=250, blank=True, verbose_name='German care instructions')
    care_instructions_en            = models.TextField(max_length=250, blank=True, verbose_name='English care instructions')
    care_instructions_it            = models.TextField(max_length=250, blank=True, verbose_name='Italian care instructions')

    color_1                         = models.CharField(max_length=50, blank=False, verbose_name='Main color')
    color_2                         = models.CharField(max_length=50, blank=True, verbose_name='2nd color')
    color_3                         = models.CharField(max_length=50, blank=True, verbose_name='3rd color')
    color_4                         = models.CharField(max_length=50, blank=True, verbose_name='4th color')
    fabric_1                        = models.CharField(max_length=50, blank=False, verbose_name='Main fabric')
    fabric_2                        = models.CharField(max_length=50, blank=True, verbose_name='2nd fabric')
    fabric_3                        = models.CharField(max_length=50, blank=True, verbose_name='3rd fabric')
    fabric_4                        = models.CharField(max_length=50, blank=True, verbose_name='4th fabric')
    fabric_1_percentage             = models.IntegerField(default=100, blank=True, verbose_name='Percentage main fabric', help_text='Percentage of the main fabric in %')
    fabric_2_percentage             = models.IntegerField(blank=True, verbose_name='Percentage 2nd fabric', help_text='Percentage of 2nd fabric in %')
    fabric_3_percentage             = models.IntegerField(blank=True, verbose_name='Percentage 3rd fabric', help_text='Percentage of 3rd fabric in %')
    fabric_4_percentage             = models.IntegerField(blank=True, verbose_name='Percentage 4th fabric', help_text='Percentage of 4th fabric in %')
    weight                          = models.SmallIntegerField(blank=True, help_text='Product weight in grams')
    surface_weight                  = models.SmallIntegerField(blank=True, help_text='Product surface weight in grams/m²')

    def __unicode__(self):
        return self.name_en

    class Meta:
        ordering            = ('-name_en',)
        app_label           = 'api'
        verbose_name        = 'Product variant'
        verbose_name_plural = 'Product variants'


class Product_variant_serializer(serializers.HyperlinkedModelSerializer):

    def __unicode__(self):
        return self.id

    class Meta:
        model  = Product_variant
        fields = (
                  'created',
                  'updated',
                  'is_active',
                  'is_organic',
                  'name_en', 'name_de', 'name_it',
                  'description_de', 'description_en', 'description_it',
                  'care_instructions_de', 'care_instructions_en', 'care_instructions_it',
                  'rec_gross_sale_price_default',
                  'size',
                  'color_1','color_2','color_3','color_4',
                  'fabric_1','fabric_2','fabric_3','fabric_4',
                  'fabric_1_percentage','fabric_2_percentage','fabric_3_percentage','fabric_4_percentage',
                  'weight', 'surface_weight'
                 )
