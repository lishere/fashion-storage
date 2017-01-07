# -*- coding: utf-8 -*-

from django.db import models

from api.models.country import Country


class Customer(models.Model):

    GENDER          = (('F','Female'),('M','Male'))
    LANGUAGES       = (('DE','German'),('EN','English'))

    created             = models.DateTimeField(auto_now_add=True, blank=False)
    updated             = models.DateTimeField(auto_now_add=True, blank=True)
    is_active           = models.BooleanField(default=True, blank=True)
    items_bought        = models.IntegerField(default=0, blank=True)
    wants_newsletter    = models.BooleanField(default=True, blank=True)
    language            = models.CharField(max_length=2, default='DE', choices=LANGUAGES, blank=False)

    gender              = models.CharField(max_length=1, default='F', choices=GENDER, blank=False)
    given_name          = models.CharField(max_length=50, blank=False)
    surname             = models.CharField(max_length=50, blank=False)

    phone               = models.CharField(max_length=50, blank=True)
    email               = models.EmailField(max_length=50, blank=True)

    address             = models.CharField(max_length=125, blank=True)
    zip_code            = models.CharField(max_length=50, blank=True)
    city                = models.CharField(max_length=50, blank=True)
    country             = models.ForeignKey(Country, blank=True)

    facebook            = models.URLField(max_length=250, blank=True)
    twitter             = models.URLField(max_length=250, blank=True)
    instagram           = models.URLField(max_length=250, blank=True)
    pinterest           = models.URLField(max_length=250, blank=True)

    def __unicode__(self):
        return '%s %s' % (self.given_name, self.surname)

    class Meta:
        ordering    = ('given_name','surname',)
        app_label   = 'api'