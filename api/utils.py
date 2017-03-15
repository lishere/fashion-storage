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

def getQuantityForProductVariantInListing(productVariantId, listingId):
    listing = Listing.objects.get(id=listingId, product_variant_id=productVariantId)
    return listing.quantity

def getProductVariantsForProductMove(productMoveId):
    listings = getListingsForProductMove(productMoveId)
    pv_ids   = getProductVariantIdsForListings(listings)

    product_variants = []
    for p in pv_ids:
        product = getProductByProductVariantId(p)
        pv = g(Product_variant, p)
        product_variants.append(
            product.type.capitalize()+' '+
            product.name+' '+
            pv.fabric_1_de+' '+
            pv.size
            # getQuantityForProductVariantInListing(p, listingId)
        )
    return product_variants

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
    pv = g(Product_variant, productVariantId)
    return Product.objects.get(id=pv.product_id)
