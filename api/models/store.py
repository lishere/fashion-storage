# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import serializers

from api.models.country import Country
from api.models.invoice_address import Invoice_address
from api.models.shipping_address import Shipping_address


class Store(models.Model):

    SHIPPING_AGREMENTS = (('store_pays', 'Store pays shippings costs'),('split', 'Shipping costs are split'),('we_pay', 'We pay shipping costs'),)
    PARTNER_TYPES = (('commission','Commission'),('direct_buyer','Direct buyer'),('mixed','Mixed'),)

    created             = models.DateTimeField(auto_now_add=True, blank=False)
    updated             = models.DateTimeField(auto_now_add=True, blank=True)
    is_active           = models.BooleanField(default=True, blank=True)
    is_online_shop      = models.BooleanField(default=False, blank=True)
    is_agency           = models.BooleanField(default=False, blank=True, help_text='Is this partner an agency?')
    in_acquisition      = models.BooleanField(default=False, blank=True)

    name                = models.CharField(max_length=250, blank=False)
    address             = models.CharField(max_length=125, blank=True)
    zip_code            = models.CharField(max_length=50, blank=True)
    city                = models.CharField(max_length=50, blank=False)
    country             = models.ForeignKey(Country, blank=True)

    invoice_address     = models.ForeignKey(Invoice_address, default=1, blank=True, null=True)
    shipping_address    = models.ForeignKey(Shipping_address, default=1, blank=True, null=True)

    shipping_agrement   = models.CharField(max_length=20, default='split', choices=SHIPPING_AGREMENTS, blank=True)
    partner_type        = models.CharField(max_length=20, choices=PARTNER_TYPES, blank=True)
    commission_rate     = models.IntegerField(default=50, blank=True, help_text='Commmission as charged by this partner in %')

    website             = models.URLField(max_length=250, blank=True)
    facebook            = models.URLField(max_length=250, blank=True)
    twitter             = models.URLField(max_length=250, blank=True)
    instagram           = models.URLField(max_length=250, blank=True)
    pinterest           = models.URLField(max_length=250, blank=True)

    # stock

    def __unicode__(self):
        return self.name

    class Meta:
        ordering    = ('name',)
        app_label   = 'api'
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

class Store_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = ('created',
                  'updated',
                  'is_active',
                  'is_online_shop',
                  'in_acquisition',
                  'name',
                  'address',
                  'zip_code',
                  'city',
                  'country',
                  'invoice_address',
                  'shipping_address',
                  'shipping_agrement',
                  'partner_type',
                  'commission_rate',
                  'website',
                  'facebook',
                  'pinterest',
                  'instagram',
                  'twitter')
