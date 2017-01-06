
# -*- coding: utf-8 -*-

from django.db import models
from api.models.country import Country

class Store(models.Model):

    SHIPPING_AGREMENTS = (('store_pays', 'Store pays shippings costs'),('split', 'Shipping costs are split'),('we_pay', 'We pay shipping costs'),)
    PARTNER_TYPES = (('commission','Commission'),('direct_buyer','Direct buyer'),('mixed','Mixed'),)

    created             = models.DateTimeField(auto_now_add=True, blank=False)
    updated             = models.DateTimeField(auto_now_add=True, blank=True)
    is_active           = models.BooleanField(default=True, blank=True)

    is_online_shop      = models.BooleanField(default=False, blank=True)
    name                = models.CharField(max_length=250, blank=False)
    address             = models.CharField(max_length=125, blank=True)
    zip_code            = models.CharField(max_length=50, blank=True)
    city                = models.CharField(max_length=50, blank=False)
    country             = models.ForeignKey(Country, blank=True)
    shipping_agrement   = models.CharField(max_length=20, choices=SHIPPING_AGREMENTS, blank=True)
    partner_type        = models.CharField(max_length=20, choices=PARTNER_TYPES, blank=True)
    commission_rate     = models.IntegerField(default=50, blank=True)
    website             = models.URLField(blank=True)
    facebook            = models.URLField(blank=True)

    class Meta:
        ordering    = ('name',)
        app_label   = 'api'
