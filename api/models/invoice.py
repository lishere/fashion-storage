# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from rest_framework import serializers

from api.models.sale import Sale


class Invoice(models.Model):

    STATES = (('paid','Paid'),('open','Open'),('chancelled','Chancelled'),)

    created                 = models.DateTimeField(auto_now_add=True, blank=False)
    updated                 = models.DateTimeField(auto_now_add=True, blank=True)
    is_active               = models.BooleanField(default=True, blank=True)

    date                    = models.DateTimeField(default=datetime.now, blank=False)
    state                   = models.CharField(default="open", max_length=20, choices=STATES, blank=True)
    correction_for          = models.ForeignKey("self", related_name="selfref", blank=True, null=True)
    discount_description    = models.TextField(blank=True, null=True)
    discount_amount         = models.IntegerField(default=0, blank=True, null=True, help_text='Discount amount as a positive number')

    sale                    = models.ForeignKey(Sale, blank=True, null=True)

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
                    'discount_amount',
                    'discount_description',
                 )
