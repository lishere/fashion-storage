# -*- coding: utf-8 -*-

from rest_framework import viewsets

from django.http import HttpResponse
from django.views.generic import TemplateView
from django_tables2 import SingleTableView, RequestConfig
from django_filters.views import FilterView

from api.models.core_data import Core_data, Core_data_serializer
from api.models.customer import Customer, Customer_serializer
from api.models.country import Country, Country_serializer
from api.models.store import Store, Store_serializer
from api.models.shipping_address import Shipping_address, Shipping_address_serializer
from api.models.invoice_address import Invoice_address, Invoice_address_serializer
from api.models.person import Person, Person_serializer
from api.models.note import Note, Note_serializer
from api.models.product import Product, Product_serializer
from api.models.product_variant import Product_variant, Product_variant_serializer
from api.models.product_variant_price_per_country import Product_variant_price_per_country, Product_variant_price_per_country_serializer
from api.models.product_variant_price_per_store import Product_variant_price_per_store, Product_variant_price_per_store_serializer
from api.models.product_move import Product_move, Product_move_serializer
from api.models.sale import Sale, Sale_serializer
from api.models.listing import Listing, Listing_serializer
from api.models.image import Image, Image_serializer
from api.models.stock import Stock, Stock_serializer
from api.models.packing_list import Packing_list, Packing_list_serializer
from api.models.invoice import Invoice, Invoice_serializer

from api.utils import getProductVariantsForInvoice, getProductVariantsForProductMove, getProductVariantIdsAndListingIdsForListings, getListingsForProductMove

from api.tables import *
from api.filters import *


# """
# Generic views
# """
#
# class FilterTableView(FilterView, SingleTableView):
#     def get_table_data(self):
#         self.filter = self.filter_class(self.request.GET, queryset =super(FilterTableView, self).get_table_data() )
#         return self.filter.qs
#

"""
Print views
"""

class InvoiceView(TemplateView):
    template_name = 'invoice-de.html'

    def get_context_data(self, **kwargs):
        context             = super(InvoiceView, self).get_context_data(**kwargs)

        id                  = self.kwargs.get('id', None)
        template_language   = self.kwargs.get('language', None)

        invoice             = Invoice.objects.get(id=id)
        product_variants    = getProductVariantsForInvoice(invoice.id)

        context['id']               = id
        context['date']             = invoice.date
        context['state']            = invoice.state
        context['created']          = invoice.created
        context['updated']          = invoice.updated
        context['product_variants'] = product_variants

        return context


# class ProductMoveView(TemplateView):
#     template_name = 'product_move-de.html'
#
#     def get_context_data(self, **kwargs):
#         context                     = super(ProductMoveView, self).get_context_data(**kwargs)
#
#         id                          = self.kwargs.get('id', None)
#         template_language           = self.kwargs.get('language', None)
#
#         product_variants            = getProductVariantsForProductMove(id)
#         context['product_variants'] = product_variants
#
#         return context

"""
List views
"""

class ProductMovesView(SingleTableView):
    template_name   = 'product_moves.html'
    model           = Product_move
    table_class     = ProductMovesTable

class SalesView(SingleTableView):
    template_name   = 'sales.html'
    model           = Sale
    table_class     = SalesTable

class StocksView(SingleTableView):
    template_name   = 'stocks.html'
    model           = Stock
    table_class     = StocksTable
    filter_class    = StocksFilter

    def get_table_data(self):
        data = super(StocksView, self).get_table_data()
        self.filter = self.filter_class(self.request.GET, queryset=data)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(StocksView, self).get_context_data(**kwargs)
        context['filter'] = self.filter.form
        return context

    # def get_context_data(self, **kwargs):
    #     context = super(StocksView, self).get_context_data(**kwargs)
    #     f = StocksFilter(self.request.GET, queryset=Stock.objects.get(id=12) , request=self.request )
    #     context['form'] = f.form
    #     return context

"""
API endpoints
"""

class CoreDataViewSet(viewsets.ModelViewSet):
    queryset = Core_data.objects.all().order_by('created')
    serializer_class = Core_data_serializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('created')
    serializer_class = Customer_serializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('-name')
    serializer_class = Country_serializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all().order_by('created')
    serializer_class = Store_serializer

class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = Shipping_address.objects.all().order_by('created')
    serializer_class = Shipping_address_serializer

class InvoiceAddressViewSet(viewsets.ModelViewSet):
    queryset = Invoice_address.objects.all().order_by('created')
    serializer_class = Invoice_address_serializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('created')
    serializer_class = Person_serializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('created')
    serializer_class = Note_serializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('created')
    serializer_class = Product_serializer

class ProductVariantViewSet(viewsets.ModelViewSet):
    queryset = Product_variant.objects.all().order_by('created')
    serializer_class = Product_variant_serializer

class ProductVariantPricePerCountryViewSet(viewsets.ModelViewSet):
    queryset = Product_variant_price_per_country.objects.all().order_by('country')
    serializer_class = Product_variant_price_per_country_serializer

class ProductVariantPricePerStoreViewSet(viewsets.ModelViewSet):
    queryset = Product_variant_price_per_store.objects.all().order_by('store')
    serializer_class = Product_variant_price_per_store_serializer

class ProductMoveViewSet(viewsets.ModelViewSet):
    queryset = Product_move.objects.all().order_by('move_date')
    serializer_class = Product_move_serializer

class PackingListViewSet(viewsets.ModelViewSet):
    queryset = Packing_list.objects.all().order_by('date')
    serializer_class = Packing_list_serializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all().order_by('created')
    serializer_class = Listing

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('created')
    serializer_class = Image_serializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all().order_by('id')
    serializer_class = Stock_serializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().order_by('id')
    serializer_class = Sale_serializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('date')
    serializer_class = Invoice_serializer
