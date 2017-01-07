# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models.country import Country
from .models.store import Store
from .models.note import Note
from .models.invoice_address import Invoice_address
from .models.person import Person
from .models.customer import Customer


class NoteInline(GenericTabularInline):
    model = Note


# Add inline notes to forms
class StoreAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

class InvoiceAddressAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

class PersonAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]


admin.site.register(Country)
admin.site.register(Store, StoreAdmin)
admin.site.register(Note)
admin.site.register(Invoice_address, InvoiceAddressAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Customer, CustomerAdmin)
