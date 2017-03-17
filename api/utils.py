# -*- coding: utf-8 -*-

from django.utils.safestring import mark_safe

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


##################### General utils

# get object providing type and id
def g(type, id):
    return type.objects.get(id=id)

##################### Get path conventions

def getAdminBasePath():
    return '/admin/api/'

def getViewBasePath():
    return '/view/'

def getEditLink(type, id):
    path = getAdminChangePathforObject(type, id)
    return mark_safe('<a href="'+str(path)+'" target="_blank">Edit</a>')

def getAddLink(type):
    path = getAdminAddPathforObject(type)
    type = str(type).replace('_', '-')
    return mark_safe('<a href="'+str(path)+'" target="_blank">Add '+str(type).lower().replace('_', '-')+'</a>')

def getAdminChangePathforObject(type, id):
    bp = getAdminBasePath()
    return str(bp)+str(type).lower()+'/'+str(id)+'/change/'

def getAdminAddPathforObject(type):
    bp = getAdminBasePath()
    return str(bp)+str(type).lower()+'/add/'

def getViewPathforObject(type, id, language='en'):
    type = str(type).replace('_', '-')
    bp = getViewBasePath()
    return str(bp)+str(type).lower()+'s/'+str(language)+'/'+str(id)


##################### Invoice utils

def getListingsForInvoice(invoiceId):
    return getListingsForProductMove(getProductMoveIdForInvoice(invoiceId))

def getProductVariantsForInvoice(invoiceId):
    return getProductVariantsForProductMove(getProductMoveIdForInvoice(invoiceId))

##################### Sale utils

def getSaleIdForInvoice(invoiceId):
    invoice = g(Invoice, invoiceId)
    return invoice.sale_id

##################### Product moves and listing utils

def getProductMoveIdForSale(saleId):
    sale = Sale.objects.get(id=saleId)
    return sale.product_move_id

def getListingsForProductMove(productMoveId):
    return Listing.objects.filter(product_move_id_id=productMoveId)

def getProductMoveId(saleId):
    sale = Sale.objects.get(id=saleId)
    return sale.product_move_id

def getProductMoveIdForInvoice(invoiceId):
    saleId = getSaleIdForInvoice(invoiceId)
    return getProductMoveIdForSale(saleId)

###################### Product variant utils

def getProductVariantIdForListing(listingId):
    listing = Listing.objects.get(id=listingId)
    return listing.product_variant_id

def getProductVariantIdsForListings(listings):
    productVariants = []
    for l in listings:
        pv = getProductVariantIdForListing(l.id)
        productVariants.append(pv)
    return productVariants

# returns array of tuples of product variant ID and listing ID
def getProductVariantIdsAndListingIdsForListings(listings):
    pv_ids_and_list_ids = []
    for l in listings:
        pv_id = getProductVariantIdForListing(l.id)
        pv_ids_and_list_ids.append([pv_id, l.id])
    return pv_ids_and_list_ids

def getQuantityForProductVariantInListing(productVariantId, listingId):
    listing = Listing.objects.get(id=listingId, product_variant_id=productVariantId)
    return listing.quantity

# returns array of tuples of product_variant ID and text
def getProductVariantsForProductMove(productMoveId):

    from api.utils import getQuantityForProductVariantInListing, getProductByProductVariantId, g

    listings            = getListingsForProductMove(productMoveId)
    pv_ids_and_list_ids = getProductVariantIdsAndListingIdsForListings(listings)
    print pv_ids_and_list_ids

    product_variants = []
    for obj in pv_ids_and_list_ids:
        pv_id       = obj[0]
        list_id     = obj[1]
        quantity    = getQuantityForProductVariantInListing(pv_id, list_id)
        product     = getProductByProductVariantId(pv_id)
        pv          = g(Product_variant, pv_id)

        if quantity != 0:
            product_variants.append([pv_id,
                product.type.capitalize()+' '+
                product.name+' '+
                pv.color_1_en+' '+
                pv.color_2_en+' '+
                pv.color_3_en+' '+
                pv.fabric_1_en+' '+
                pv.fabric_2_en+' '+
                pv.size.upper()+' '+
                '-- Quantity: '+str(quantity)]
            )

    return product_variants

def getListingsHtmlForProductMove(productMoveId):
    product_variants = getProductVariantsForProductMove(productMoveId)
    for i, pv in enumerate(product_variants):
        path = getViewPathforObject('Product_variant', pv[0])
        product_variants[i] = '<a href="'+path+'">'+pv[1]+'</a>'

    product_variants = '<br />'.join(product_variants)
    return mark_safe(product_variants)

def getListingsHtmlForSale(saleId):
    product_variants = getProductVariantsForProductMove(getProductMoveIdForSale(saleId))
    for i, pv in enumerate(product_variants):
        path = getViewPathforObject('Product_variant', pv[0])
        product_variants[i] = '<a href="'+path+'">'+pv[1]+'</a>'

    product_variants = '<br />'.join(product_variants)
    return mark_safe(product_variants)

def getProductVariantPrice(productVariantId):
    pv = Product_variant.objects.get(id=productVariantId)
    return pv.rec_gross_sale_price_default

def getProductVariantPriceByCountry(productVariantId, countryId):
    pvppc = product_variant_price_per_country.objects.get(
        product_variant_id=productVariantId,
        country_id=countryId
    )
    return pvppc.rec_gross_sale_price

def getProductVariantPriceByStore(productVariantId, storeId):
    pvppc = product_variant_price_per_country.objects.get(
        product_variant_id=productVariantId,
        store_id=storeId
    )
    return pvppc.rec_gross_sale_price


###################### Product utils

def getProductByProductVariantId(productVariantId):
    pv = g(Product_variant, productVariantId)
    return Product.objects.get(id=pv.product_id)
