# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from rest_framework import serializers

from api.models.store import Store


class Product_move(models.Model):

    created                 = models.DateTimeField(auto_now_add=True, blank=False)
    updated                 = models.DateTimeField(auto_now_add=True, blank=True)

    is_destroyed            = models.BooleanField(default=False, blank=True, verbose_name="Destroyed?", help_text="Mark this item as destroyed, stolen or otherwise non-saleable")
    move_date               = models.DateTimeField(default=datetime.now, blank=False)
    remove_from             = models.ForeignKey(Store, blank=True, null=True, verbose_name='Remove from store')
    move_to                 = models.ForeignKey(Store, related_name="moveto", blank=True, null=True, verbose_name='Move to store')

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
                    'remove_from',
                    'move_to',
                 )
