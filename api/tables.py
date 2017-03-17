# -*- coding: utf-8 -*-

import django_tables2 as tables

from api.models.sale import Sale
from api.models.stock import Stock
from api.models.product_move import Product_move


class SalesTable(tables.Table):
    listings    = tables.Column(accessor='getListings', verbose_name='Listings')
    edit        = tables.Column(accessor='editLink', verbose_name='Operation')

    class Meta:
        model = Sale
        fields = ('id', 'updated', 'sale_date', 'sale_type', 'sold_to_store', 'listings', 'edit')
        attrs = {
            'class': 'table table-striped table-bordered table-hover'
        }


class StocksTable(tables.Table):
    edit = tables.Column(accessor='editLink', verbose_name='Operation')

    class Meta:
        model = Stock
        attrs = {
           'class': 'table table-striped table-bordered table-hover'
        }


class ProductMovesTable(tables.Table):
    listings    = tables.Column(accessor='getListings', verbose_name='Listings')
    edit        = tables.Column(accessor='editLink', verbose_name='Operation')

    class Meta:
        model = Product_move
        fields = ('id', 'updated', 'move_date', 'remove_from', 'move_to', 'listings', 'edit')
        attrs = {
            'class': 'table table-striped table-bordered table-hover'
        }
