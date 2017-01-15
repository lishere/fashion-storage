# -*- coding: utf-8 -*-

from rest_framework import viewsets

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
from api.models.agency import Agency, Agency_serializer

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

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().order_by('created')
    serializer_class = Sale

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all().order_by('created')
    serializer_class = Listing

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('created')
    serializer_class = Image_serializer

class AgencyViewSet(viewsets.ModelViewSet):
    queryset = Agency.objects.all().order_by('created')
    serializer_class = Agency_serializer
