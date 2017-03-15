# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from rest_framework import serializers

from api.models.store import Store
from api.models.customer import Customer
from api.models.product_move import Product_move

class Sale(models.Model):

    def getListings(self):
        from api.utils import getProductMoveIdForSale
        from api.utils import getProductVariantsForProductMove
        pv = getProductVariantsForProductMove(getProductMoveIdForSale(self.id))
        pv = ' ** '.join(pv)
        return pv

    SALE_TYPES = (('direct-sale-to-customer','Direct sale to customer'),
                  ('online-sale','Online sale'),('commission-sale','Commission sale'),
                  ('sale-to-store','Sale to store'),('sale-to-store-via-agency','Sale to store via agency'),
                  ('other','Other'))

    created                 = models.DateTimeField(auto_now_add=True, blank=False)
    updated                 = models.DateTimeField(auto_now_add=True, blank=True)

    sale_date               = models.DateTimeField(default=datetime.now, blank=False)
    sale_type               = models.CharField(max_length=20, choices=SALE_TYPES, blank=False)

    sold_to_store           = models.ForeignKey(Store, related_name="soldtostore", blank=True, null=True, verbose_name="Sold in store / Sold to store")
    sold_to_customer        = models.ForeignKey(Customer, related_name="soldtocustomer", blank=True, null=True)
    #agency_involved         = models.ForeignKey(Agency, related_name="agencyinvolved", blank=True, null=True)

    product_move             = models.ForeignKey(Product_move, blank=True, null=True)
    # sale_amount
    # sale


    def __unicode__(self):
        return '%s %s %s %s' % (self.sale_date, self.sale_type, self.sold_to_store, self.sold_to_customer)

    class Meta:
        ordering            = ('sale_date',)
        app_label           = 'api'
        verbose_name        = 'Sale'
        verbose_name_plural = 'Sales'


class Sale_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sale
        fields = (
                    'created',
                    'updated',
                    'sale_date',
                    'sale_type',
                    'sold_to_store',
                    'sold_to_customer',
                    'product_move',
                 )
