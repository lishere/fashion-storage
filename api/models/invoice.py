# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from rest_framework import serializers

from api.models.sale import Sale


class Invoice(models.Model):

    STATES = (('paid','Paid'),('open','Open'),('chancelled','Chancelled'),)
    CURRENCIES = (('other','Other currency'),('EUR','Euro'),('GBP','British Pound'),('CAD', 'Canadian Dollar'),('DKK','Danish Krone'),('NOK','Norwegian Krone'),('RUB','Russian Rubel'),('SEK','Swedish Krona'),('CHF','Swiss Franken'),('USD','US Dollar'),)

    created                 = models.DateTimeField(auto_now_add=True, blank=False)
    updated                 = models.DateTimeField(auto_now_add=True, blank=True)
    is_active               = models.BooleanField(default=True, blank=True)

    # invoice number
    date                    = models.DateTimeField(default=datetime.now, blank=False)
    state                   = models.CharField(default="open", max_length=20, choices=STATES, blank=True)
    correction_for          = models.ForeignKey("self", related_name="selfref", blank=True, null=True, help_text='Choose here if this invoice is a correction for a previous invoice')
    sale                    = models.ForeignKey(Sale, blank=True, null=True)
    sale_vat                = models.IntegerField(default=19, blank=True, null=True, verbose_name='Sale VAT', help_text='VAT to apply on all items in sale in %')
    other_items             = models.TextField(blank=True, null=True, help_text='You can add items not included in a sale. Add description for other items here')
    other_items_amount      = models.IntegerField(default=0, blank=True, null=True, help_text='Add other items amount')
    other_items_vat         = models.IntegerField(default=19, blank=True, null=True, verbose_name='Other items VAT', help_text='VAT to apply on other items in %')
    discount_description    = models.TextField(blank=True, null=True)
    discount_amount         = models.IntegerField(default=0, blank=True, null=True, help_text='Discount amount as a positive number')
    general_description     = models.TextField(blank=True, null=True, verbose_name='Other text', help_text='Other text to add to this invoice')
    currency                = models.CharField(default='EUR', max_length=3, choices=CURRENCIES, blank=True)

    # total_vat_amount
    # total_invoice_amount

    def __unicode__(self):
        return '%s %s %s' % (self.id, self.date, self.state)

    class Meta:
        ordering            = ('date',)
        app_label           = 'api'
        verbose_name        = 'Invoice'
        verbose_name_plural = 'Invoices'


class Invoice_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = (
                    'created',
                    'updated',
                    'is_active',
                    'date',
                    'state',
                    'correction_for',
                    'sale',
                    'sale_vat',
                    'other_items',
                    'other_items_description',
                    'discount_amount',
                    'discount_description',
                 )
