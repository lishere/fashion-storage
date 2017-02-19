# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from django.db.models.signals import post_save
from rest_framework import serializers

from api.models.product_move import Product_move
from api.models.product_variant import Product_variant
from api.models.store import Store
from api.models.listing import Listing


# Increment or decrement the number of products in a store's stock.
# Implemented using Django signals, triggered after a listing is saved.
#
def modify_stock(sender, instance, **kwargs):

    # check if a product_move is associated with this listing instance, if not return
    try:
        product_move = Product_move.objects.get(id=instance.product_move_id_id)
        print("Incrementing stock according to product move with ID "+str(product_move.id)+
              " after listing with ID "+str(instance.id)+" has been saved.")
    except Product_move.DoesNotExist:
        print("Listing saved, no product has been moved.")
        return

    product_variant = Product_variant.objects.get(id=instance.product_variant_id)
    product_variant_name = str(product_variant.product)+" "+str(product_variant.color_1_en)+" "+str(product_variant.color_2_en)+" "+str(product_variant.fabric_1_en)+" "+str(product_variant.size.upper())

    # check if we should increment a stock and if the stock to be incremented exists
    if product_move.move_to_id:
        try:
            stock_to_increment = Stock.objects.get(product_variant_id=instance.product_variant_id,
                                                   store_id=product_move.move_to_id)
            # save to db
            Stock(product_variant_id=instance.product_variant_id,
                               quantity=stock_to_increment.quantity+instance.quantity,
                               store_id=product_move.move_to_id).save()
            print("Successfully incremented stock from "+str(stock_to_increment.quantity)+
                  " items to "+str(instance.quantity)+
                  " for product "+str(product_variant_name)+
                  " in store with id "+str(product_move.move_to_id))

        except Stock.DoesNotExist:
            Stock(product_variant_id=instance.product_variant_id,
                  quantity=instance.quantity,
                  store_id=product_move.move_to_id).save()

    # check if we should decrement a stock and if the stock to be decremented exists
    if product_move.remove_from_id:
        try:
            stock_to_decrement = Stock.objects.get(product_variant_id=instance.product_variant_id,
                                                   store_id=product_move.remove_from_id)
            # save to db
            Stock(product_variant_id=instance.product_variant_id,
                               quantity=stock_to_decrement.quantity-instance.quantity,
                               store_id=product_move.remove_from_id).save()
            print("Successfully decremented stock from "+str(stock_to_decrement.quantity)+
                  " items to "+str(instance.quantity)+
                  " for product "+str(product_variant_name)+
                  " in store with id "+str(product_move.remove_from_id))

        except Stock.DoesNotExist:
            Stock(product_variant_id=instance.product_variant_id,
                  quantity=instance.quantity,
                  store_id=product_move.remove_from_id).save()

post_save.connect(modify_stock, sender=Listing)


class Stock(models.Model):

    created                  = models.DateTimeField(auto_now_add=True, blank=False)
    updated                  = models.DateTimeField(auto_now_add=True, blank=True)

    store                    = models.ForeignKey(Store, blank=False, null=False)
    product_variant          = models.ForeignKey(Product_variant, blank=False, null=False)
    quantity                 = models.DecimalField(default=0, max_digits=10, decimal_places=0, blank=True, null=True)

    def __unicode__(self):
        return '%s %s %s %s' % (self.id, self.store, self.product_variant, self.quantity)

    class Meta:
        ordering            = ('created',)
        app_label           = 'api'
        verbose_name        = 'Stock'
        verbose_name_plural = 'Stocks'


class Stock_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = (
                    'created',
                    'updated',
                    'store',
                    'product_variant',
                    'quantity'
                 )
