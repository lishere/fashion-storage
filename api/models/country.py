from django.db import models
#from django.contrib.contenttypes import *

#import api.lists.country_list
#import api.lists.store_list

class Country(models.Model):
    #name                = models.CharField(max_length=3, choices=api.lists.country_list.COUNTRIES, primary_key=True)
    created             = models.DateTimeField(auto_now_add=True)
    vat_rate            = models.IntegerField(default=0)
    #category            = models.CharField(max_length=20, choices=api.lists.country_list.CATEGORIES)
    # internal note
    #currency            = models.CharField(max_length=3, choices=api.lists.country_list.CURRENCIES)

    class Meta:
    #    ordering    = 'name'
        app_label   = 'api'
