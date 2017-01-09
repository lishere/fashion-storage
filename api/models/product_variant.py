# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import serializers

from api.models.image import Image
from api.models.product import Product


class Product_variant(models.Model):

    SIZES = (('unisize','Unisize'),('s','S'),('xs','XS'),('m','M'),('l','L'),('xl','XL'),('xxl','XXL'),('ws','Women S'),('wxs','Women XS'),('wm','Women M'),('wl','Women L'),('wxl','Women XL'),('ms','Men S'),('mxs','Men XS'),('mm','Men M'),('ml','Men L'),('mxl','Men XL'),('mxxl','Men XXL'),)

    created                         = models.DateTimeField(auto_now_add=True, blank=False)
    updated                         = models.DateTimeField(auto_now_add=True, blank=True)
    is_active                       = models.BooleanField(default=True, blank=True)
    is_organic                      = models.BooleanField(default=False, blank=False, verbose_name="Organic", help_text="Is this product variant made from organic materials?")

    product                         = models.ForeignKey(Product, default=1, blank=False)
    images                          = models.ManyToManyField(Image, blank=True)

    rec_gross_sale_price_default    = models.DecimalField(default=0, max_digits=6, decimal_places=2, blank=True, verbose_name='Recommended default gross sale price')
    # rec_gross_sale_price_by_country
    size                            = models.CharField(max_length=7, default='unisize', choices=SIZES, blank=False)

    description_de                  = models.TextField(max_length=500, blank=True, verbose_name='German description')
    description_en                  = models.TextField(max_length=500, blank=True, verbose_name='English description')
    description_it                  = models.TextField(max_length=500, blank=True, verbose_name='Italian description')
    care_instructions_de            = models.TextField(max_length=250, blank=True, verbose_name='German care instructions')
    care_instructions_en            = models.TextField(max_length=250, blank=True, verbose_name='English care instructions')
    care_instructions_it            = models.TextField(max_length=250, blank=True, verbose_name='Italian care instructions')

    color_1_de                      = models.CharField(max_length=50, blank=False, verbose_name='Main color in German')
    color_1_en                      = models.CharField(max_length=50, blank=False, verbose_name='Main color in English')
    color_1_it                      = models.CharField(max_length=50, blank=False, verbose_name='Main color in Italian')
    color_2_de                      = models.CharField(max_length=50, blank=True, verbose_name='2nd color in German')
    color_2_en                      = models.CharField(max_length=50, blank=True, verbose_name='2nd color in English')
    color_2_it                      = models.CharField(max_length=50, blank=True, verbose_name='2nd color in Italian')
    color_3_de                      = models.CharField(max_length=50, blank=True, verbose_name='3rd color in German')
    color_3_en                      = models.CharField(max_length=50, blank=True, verbose_name='3rd color in English')
    color_3_it                      = models.CharField(max_length=50, blank=True, verbose_name='3rd color in Italian')
    color_4_de                      = models.CharField(max_length=50, blank=True, verbose_name='4th color in German')
    color_4_en                      = models.CharField(max_length=50, blank=True, verbose_name='4th color in English')
    color_4_it                      = models.CharField(max_length=50, blank=True, verbose_name='4th color in Italian')

    fabric_1_de                     = models.CharField(max_length=50, blank=False, verbose_name='Main fabric in German')
    fabric_1_en                     = models.CharField(max_length=50, blank=False, verbose_name='Main fabric in English')
    fabric_1_it                     = models.CharField(max_length=50, blank=False, verbose_name='Main fabric in Italian')
    fabric_2_de                     = models.CharField(max_length=50, blank=True, verbose_name='2nd fabric in German')
    fabric_2_en                     = models.CharField(max_length=50, blank=True, verbose_name='2nd fabric in English')
    fabric_2_it                     = models.CharField(max_length=50, blank=True, verbose_name='2nd fabric in Italian')
    fabric_3_de                     = models.CharField(max_length=50, blank=True, verbose_name='3nd fabric in German')
    fabric_3_en                     = models.CharField(max_length=50, blank=True, verbose_name='3nd fabric in English')
    fabric_3_it                     = models.CharField(max_length=50, blank=True, verbose_name='3nd fabric in Italian')
    fabric_4_de                     = models.CharField(max_length=50, blank=True, verbose_name='4nd fabric in German')
    fabric_4_en                     = models.CharField(max_length=50, blank=True, verbose_name='4nd fabric in English')
    fabric_4_it                     = models.CharField(max_length=50, blank=True, verbose_name='4nd fabric in Italian')
    fabric_1_percentage             = models.IntegerField(default=100, blank=True, verbose_name='Percentage main fabric', help_text='Percentage of the main fabric in %')
    fabric_2_percentage             = models.IntegerField(default=0, blank=True, verbose_name='Percentage 2nd fabric', help_text='Percentage of 2nd fabric in %')
    fabric_3_percentage             = models.IntegerField(default=0, blank=True, verbose_name='Percentage 3rd fabric', help_text='Percentage of 3rd fabric in %')
    fabric_4_percentage             = models.IntegerField(default=0, blank=True, verbose_name='Percentage 4th fabric', help_text='Percentage of 4th fabric in %')

    weight                          = models.SmallIntegerField(default=0, blank=True, help_text='Product weight in grams')
    surface_weight                  = models.SmallIntegerField(default=0, blank=True, help_text='Product surface weight in grams/m²')

    def __unicode__(self):
        return '%s %s %s %s %s' % ( self.product, self.color_1_en, self.color_2_en, self.fabric_1_en, self.size.upper())

    class Meta:
        ordering            = ('created',)
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
                  'images',
                  'description_de', 'description_en', 'description_it',
                  'care_instructions_de', 'care_instructions_en', 'care_instructions_it',
                  'rec_gross_sale_price_default',
                  'size',
                  'color_1_de','color_2_de','color_3_de','color_4_de',
                  'color_1_en','color_2_en','color_3_en','color_4_en',
                  'color_1_it','color_2_it','color_3_it','color_4_it',
                  'fabric_1_de','fabric_2_de','fabric_3_de','fabric_4_de',
                  'fabric_1_en','fabric_2_en','fabric_3_en','fabric_4_en',
                  'fabric_1_it','fabric_2_it','fabric_3_it','fabric_4_it',
                  'fabric_1_percentage','fabric_2_percentage','fabric_3_percentage','fabric_4_percentage',
                  'weight', 'surface_weight'
                 )
