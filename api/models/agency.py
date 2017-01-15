# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import serializers

from api.models.country import Country
from api.models.person import Person
from api.models.store import Store


class Agency(models.Model):

    created             = models.DateTimeField(auto_now_add=True, blank=False)
    updated             = models.DateTimeField(auto_now_add=True, blank=True)
    is_active           = models.BooleanField(default=True, blank=True)
    in_acquisition      = models.BooleanField(default=False, blank=True)

    name                = models.CharField(max_length=250, blank=False)
    contact_person      = models.ForeignKey(Person, default=1, blank=False)
    address             = models.CharField(max_length=125, blank=True)
    zip_code            = models.CharField(max_length=50, blank=True)
    city                = models.CharField(max_length=50, blank=False)
    country             = models.ForeignKey(Country, blank=True, default="DE")
    stores              = models.ManyToManyField(Store, blank=True, help_text='Select the stores which are connected to this agency')
    commission_rate     = models.IntegerField(default=50, blank=True, help_text='Commmission as charged by the agency in %')
    website             = models.URLField(max_length=250, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering    = ('name',)
        app_label   = 'api'
        verbose_name = 'Agency'
        verbose_name_plural = 'Agencies'

class Agency_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agency
        fields = ('created',
                  'updated',
                  'is_active',
                  'in_acquisition',
                  'name',
                  'contact_person',
                  'address',
                  'zip_code',
                  'city',
                  'country',
                  'commission_rate',
                  'website')
