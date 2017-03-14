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

def getObjectInstanceById(type, id):
    return type.objects.get(id=id)


##################### Product moves and listing utils

def getListingsForProductMove(productMoveId):
    return Listing.objects.filter(product_move_id_id=productMoveId)

def getProductMoveId(saleId):
    sale = Sale.objects.get(id=saleId)
    return sale.product_move_id


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

def getProductVariantsInProductMove(productMoveId):
    listings = getListingsForProductMove(productMoveId)

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
    pv = getObjectInstanceById(Product_variant, productVariantId)
    return Product.objects.get(id=pv.product_id)
