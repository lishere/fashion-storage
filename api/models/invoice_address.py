
# -*- coding: utf-8 -*-

from django.db import models
from api.models.country import Country


class Invoice_address(models.Model):

    created             = models.DateTimeField(auto_now_add=True, blank=False)
    updated             = models.DateTimeField(auto_now_add=True, blank=True)
    is_active           = models.BooleanField(default=True, blank=True)

    name                = models.CharField(max_length=250, blank=False)
    recipient           = models.CharField(max_length=250, blank=False)
    # contact person
    address             = models.CharField(max_length=125, blank=True)
    zip_code            = models.CharField(max_length=50, blank=True)
    city                = models.CharField(max_length=50, blank=False)
    country             = models.ForeignKey(Country, blank=True)
    vat_number          = models.CharField(max_length=250, blank=True)
    tax_number          = models.CharField(max_length=250, blank=True)

    def __unicode__(self):
        return self.get_name_display()

    class Meta:
        ordering    = ('name',)
        app_label   = 'api'
