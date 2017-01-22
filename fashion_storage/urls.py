# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'core-data', views.CoreDataViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'countries', views.CountryViewSet)
router.register(r'stores', views.StoreViewSet)
router.register(r'shipping-addresses', views.ShippingAddressViewSet)
router.register(r'invoice-addresses', views.InvoiceAddressViewSet)
router.register(r'notes', views.NoteViewSet)
router.register(r'persons', views.PersonViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'product-variants', views.ProductVariantViewSet)
router.register(r'product-variant-prices-per-country', views.ProductVariantPricePerCountryViewSet)
router.register(r'product-variant-prices-per-store', views.ProductVariantPricePerStoreViewSet)
router.register(r'product-moves', views.ProductMoveViewSet)
router.register(r'sales', views.SaleViewSet)
router.register(r'listings', views.ListingViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'stocks', views.ImageViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
