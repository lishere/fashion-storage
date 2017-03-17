# -*- coding: utf-8 -*-

from django_filters import *
from django.forms import *
import django.forms as forms

from api.models.stock import Stock

class StocksFilter(FilterSet):
    class Meta:
        model = Stock
        fields = ['id', 'store']

class StocksFilterForm(ModelForm):
    quantity = forms.DecimalField()
    class Meta:
        model = Stock
        fields = ['id']
