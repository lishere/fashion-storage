# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

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
from .models.agency import Agency


class NoteInline(GenericTabularInline):
    model = Note

class ProductVariantPricePerCountryInline(admin.TabularInline):
    model = Product_variant_price_per_country

# Add inline notes to forms
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
        NoteInline,
    ]

class AgencyAdmin(admin.ModelAdmin):
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
admin.site.register(Image, ImageAdmin)
admin.site.register(Agency, AgencyAdmin)
