# -*- coding: utf-8 -*-

from rest_framework import viewsets

from api.models.customer import Customer, Customer_serializer
from api.models.country import Country, Country_serializer
from api.models.store import Store, Store_serializer
from api.models.shipping_address import Shipping_address, Shipping_address_serializer
from api.models.invoice_address import Invoice_address, Invoice_address_serializer
from api.models.person import Person, Person_serializer
from api.models.note import Note, Note_serializer

"""
API endpoints
"""
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
