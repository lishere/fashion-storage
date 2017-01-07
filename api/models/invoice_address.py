
# -*- coding: utf-8 -*-

from django.db import models
from api.models.country import Country
from api.models.person import Person


class Invoice_address(models.Model):

    created             = models.DateTimeField(auto_now_add=True, blank=False)
    updated             = models.DateTimeField(auto_now_add=True, blank=True)
    is_active           = models.BooleanField(default=True, blank=True)

    recipient           = models.CharField(max_length=250, blank=False)
    contact_person      = models.ForeignKey(Person, default=1, blank=True)
    address             = models.CharField(max_length=125, blank=True)
    zip_code            = models.CharField(max_length=50, blank=True)
    city                = models.CharField(max_length=50, blank=False)
    country             = models.ForeignKey(Country, blank=True)
    vat_number          = models.CharField(max_length=250, blank=True)
    tax_number          = models.CharField(max_length=250, blank=True)

    def __unicode__(self):
        return '%s, %s' % (self.recipient, self.city)

    class Meta:
        ordering    = ('recipient',)
        app_label   = 'api'
