# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from rest_framework import serializers

from api.models.store import Store


class Product_move(models.Model):

    MOVE_TYPES = (('moved_to_store','Moved to store'),('non_saleable','Marked as non-saleable'),)

    created                 = models.DateTimeField(auto_now_add=True, blank=False)
    updated                 = models.DateTimeField(auto_now_add=True, blank=True)

    move_date               = models.DateTimeField(default=datetime.now, blank=False)
    move_type               = models.CharField(max_length=20, choices=MOVE_TYPES, blank=False)
    remove_from             = models.ForeignKey(Store, blank=False)
    move_to                 = models.ForeignKey(Store, related_name="moveto", blank=False)

    def __unicode__(self):
        return '%s %s %s' % (self.move_date, self.remove_from, self.move_to)

    class Meta:
        ordering            = ('move_date',)
        app_label           = 'api'
        verbose_name        = 'Product move'
        verbose_name_plural = 'Product moves'


class Product_move_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product_move
        fields = (
                    'created',
                    'updated',
                    'move_date',
                    'move_type',
                    'remove_from'
                    'move_to'
                 )
