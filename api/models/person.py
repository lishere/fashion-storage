# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from rest_framework import serializers


class Person(models.Model):

    PARTNER_TYPES   = (('seller','Seller'),('producer','Producer'),('agency','Agent'),('other','Other'))
    GENDER          = (('F','Female'),('M','Male'))
    LANGUAGES       = (('DE','German'),('EN','English'))

    created             = models.DateTimeField(auto_now_add=True, blank=False)
    updated             = models.DateTimeField(auto_now_add=True, blank=True)
    is_active           = models.BooleanField(default=True, blank=True)
    resubmission_date   = models.DateField(default=datetime.now, blank=True, null=True, help_text='Mark this data set for resubmission on a date')

    language            = models.CharField(max_length=2, default='DE', choices=LANGUAGES, blank=False)
    partner_type        = models.CharField(max_length=25, default='seller', choices=PARTNER_TYPES, blank=False)

    gender              = models.CharField(max_length=1, default='F', choices=GENDER, blank=False)
    given_name          = models.CharField(max_length=50, blank=False)
    surname             = models.CharField(max_length=50, blank=False)
    phone_1             = models.CharField(max_length=50, blank=True)
    phone_2             = models.CharField(max_length=50, blank=True)
    email_1             = models.EmailField(max_length=50, blank=True)
    email_2             = models.EmailField(max_length=50, blank=True)

    def __unicode__(self):
        return '%s %s' % (self.given_name, self.surname)

    class Meta:
        ordering    = ('given_name','surname',)
        app_label   = 'api'
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'


class Person_serializer(serializers.HyperlinkedModelSerializer):

    def __unicode__(self):
        return self.id

    class Meta:
        model = Person
        fields = ('created',
                  'updated',
                  'is_active',
                  'language',
                  'partner_type',
                  'language',
                  'gender',
                  'given_name',
                  'surname',
                  'phone_1',
                  'phone_2',
                  'email_1',
                  'email_2')
