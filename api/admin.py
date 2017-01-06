from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.

from .models.country import Country
from .models.store import Store
from .models.note import Note
from .models.invoice_address import Invoice_address

class NoteInline(GenericTabularInline):
    model = Note

class StoreAdmin(admin.ModelAdmin):
    inlines = [
        NoteInline,
    ]

admin.site.register(Country)
admin.site.register(Store, StoreAdmin)
admin.site.register(Note)
admin.site.register(Invoice_address)
