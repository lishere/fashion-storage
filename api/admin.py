from django.contrib import admin

# Register your models here.

from .models.country import Country
from .models.store import Store
from .models.note import Note

admin.site.register(Country)
admin.site.register(Store)
admin.site.register(Note)
