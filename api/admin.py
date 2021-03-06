# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models.core_data import Core_data
from .models.country import Country
from .models.store import Store
from .models.note import Note
from .models.invoice_address import Invoice_address
from .models.shipping_address import Shipping_address
from .models.person import Person
from .models.customer import Customer
from .models.product import Product
from .models.image import Image
from .models.product_variant import Product_variant
from .models.product_variant_price_per_country import Product_variant_price_per_country
from .models.product_variant_price_per_store import Product_variant_price_per_store
from .models.product_move import Product_move
from .models.sale import Sale
from .models.listing import Listing
from .models.stock import Stock, Stock_serializer
from .models.packing_list import Packing_list, Packing_list_serializer
from .models.invoice import Invoice, Invoice_serializer


# defining inlines
class NoteInline(GenericTabularInline):
    model = Note

class ProductVariantPricePerCountryInline(admin.TabularInline):
    model = Product_variant_price_per_country

class ProductVariantPricePerStoreInline(admin.TabularInline):
    model = Product_variant_price_per_store

class ListingInline(admin.TabularInline):
    model = Listing

class ProductMoveInline(admin.TabularInline):
    model = Product_move

class SaleInline(admin.TabularInline):
    model = Sale


# Add inlines to forms
class StoreAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

class InvoiceAddressAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

class ShippingAddressAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

class ImageAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [
        ProductVariantPricePerCountryInline,
        ProductVariantPricePerStoreInline,
        NoteInline,
    ]

class ProductMoveAdmin(admin.ModelAdmin):
    inlines = [
        ListingInline,
        NoteInline,
    ]

class SaleAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

class PackingListAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

admin.site.register(Country)
admin.site.register(Store, StoreAdmin)
admin.site.register(Note)
admin.site.register(Invoice_address, InvoiceAddressAdmin)
admin.site.register(Shipping_address, ShippingAddressAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Product_variant, ProductVariantAdmin)
admin.site.register(Product_variant_price_per_country)
admin.site.register(Product_variant_price_per_store)
admin.site.register(Product_move, ProductMoveAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Listing)
admin.site.register(Image, ImageAdmin)
admin.site.register(Core_data)
admin.site.register(Stock)
admin.site.register(Packing_list, PackingListAdmin)
admin.site.register(Invoice, InvoiceAdmin)
