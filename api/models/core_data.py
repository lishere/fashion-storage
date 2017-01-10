# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import serializers

from api.models.country import Country

class Core_data(models.Model):

    created                     = models.DateTimeField(auto_now_add=True, blank=False)
    updated                     = models.DateTimeField(auto_now_add=True, blank=True)

    company_name                = models.CharField(max_length=250, blank=False)
    logo                        = models.ImageField(upload_to='images', blank=True)
    contact_person              = models.CharField(max_length=250, blank=False)
    address                     = models.CharField(max_length=125, blank=False)
    zip_code                    = models.CharField(max_length=50, blank=False)
    city                        = models.CharField(max_length=50, blank=False)
    country                     = models.ForeignKey(Country, blank=True, default="DE")

    email                       = models.EmailField(max_length=50, blank=True)
    website                     = models.URLField(max_length=250, blank=True)

    banking_account_recipient   = models.CharField(max_length=100, blank=True)
    banking_account_bank        = models.CharField(max_length=100, blank=True)
    banking_account_iban        = models.CharField(max_length=100, blank=True)
    banking_account_bic         = models.CharField(max_length=100, blank=True)

    tax_number                  = models.CharField(max_length=100, blank=True, verbose_name="Tax number")
    vat_number                  = models.CharField(max_length=100, blank=True, verbose_name="VAT number")
    eori_number                 = models.CharField(max_length=100, blank=True, verbose_name="EORI number", help_text="Economic Operators’ Registration and Identification number used in customs declarations")

    def __unicode__(self):
        return self.company_name

    class Meta:
        app_label   = 'api'
        verbose_name = 'Core_data'
        verbose_name_plural = 'Core data'


class Core_data_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Core_data
        fields = ('created',
                  'updated',
                  'company_name',
                  'logo',
                  'contact_person',
                  'address',
                  'zip_code',
                  'city',
                  'country',
                  'email',
                  'website',
                  'banking_account_recipient',
                  'banking_account_bank',
                  'banking_account_iban',
                  'banking_account_bic',
                  'tax_number',
                  'vat_number',
                  'eori_number')
