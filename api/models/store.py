from django.db import models
#from django.contrib.contenttypes import *

#import api.lists.country_list
#import api.lists.store_list



class Store(models.Model):
    created             = models.DateTimeField(auto_now_add=True)
    is_active           = models.BooleanField(default=True)
    is_online_shop      = models.BooleanField(default=False)
    name                = models.CharField(max_length=250)
    address             = models.CharField(max_length=125)
    zip_code            = models.CharField(max_length=50)
    city                = models.CharField(max_length=50)
    #country             = models.ForeignKey(
    #                        Country
    #                      )
    test1            = models.CharField(max_length=50)
    # contact_person
    # shipping_address
    # invoice_address
    #shipping_agrement   = models.CharField(max_length=20, choices=api.lists.store_list.SHIPPING_AGREMENTS)
    #partner_type        = models.CharField(max_length=20, choices=api.lists.store_list.PARTNER_TYPES)
    commission_rate     = models.IntegerField(default=50)
    website             = models.URLField(blank=True)
    facebook            = models.URLField(blank=True)

    class Meta:
        ordering    = 'name'
        app_label   = 'api'
