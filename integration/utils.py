# coding=utf-8
from lxml import etree


def amz_product_feed(amz, products):
    """

    :return:
    :rtype:
    """
    feed = etree.Element('AmazonEnvelope')

    # create header
    header = etree.SubElement(feed, 'Header')
    documentver = etree.SubElement(header, 'DocumentVersion')
    documentver.text = "1.01"
    merchantidentifier = etree.SubElement(header, 'MerchantIdentifier')
    merchantidentifier.text = amz['mid']

    #MessageType
    msgtype = etree.SubElement(feed, 'MessageType')
    msgtype.text = 'Product'

    #<PurgeAndReplace>false</PurgeAndReplace>
    purgenreplace = etree.SubElement(feed, 'PurgeAndReplace')
    purgenreplace.text = "false"

    for i, product in enumerate(products):
        msg = etree.SubElement(feed, 'Message')

        msgid = etree.SubElement(msg, 'MessageID')
        msgid.text = str(i+1)

        optype = etree.SubElement(msg, 'OperationType')
        optype.text = "Update"


        prod = etree.SubElement(msg, 'Product')

        sku = etree.SubElement(prod, 'SKU')
        sku.text = product['sku']

        spid = etree.SubElement(prod, 'StandardProductID')
        sptype = etree.SubElement(spid, 'Type')
        sptype.text = product['ucodetype']
        sptypeval = etree.SubElement(spid, 'Value')
        sptypeval.text = product['ucodevalue']

        prodtaxcode = etree.SubElement(prod, 'ProductTaxCode')
        prodtaxcode.text = 'A_GEN_NOTAX'

        descdata = etree.SubElement(prod, 'DescriptionData')
        title = etree.SubElement(descdata, 'Title')
        title.text = product['title']
        brand = etree.SubElement(descdata, 'Brand')
        brand.text = product['brand']
        description = etree.SubElement(descdata, 'Description')
        description.text = product['desc']
        bulletpoint = etree.SubElement(descdata, 'BulletPoint')
        bulletpoint.text = product['bulletpoint1']
        bulletpoint = etree.SubElement(descdata, 'BulletPoint')
        bulletpoint.text = product['bulletpoint2']
        MSRP = etree.SubElement(descdata, 'MSRP', currency="USD")
        MSRP.text = str(product['MSRP'])
        manufacturer = etree.SubElement(descdata, 'Manufacturer')
        manufacturer.text = product['manufacturer']

        for item in product['itemtypes']:
            itemtype = etree.SubElement(descdata, 'ItemType')
            itemtype.text = item

        pdata = etree.SubElement(prod, 'ProductData')
        pcat = etree.SubElement(pdata, product['pdata'])
        ptype = etree.SubElement(pcat, 'ProductType')
        ptype = etree.SubElement(ptype, product['ptype'])

    feedstring = etree.tostring(feed)
    feedstring.replace("<AmazonEnvelope>", '<AmazonEnvelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="amzn- envelope.xsd">')
    header = '<?xml version="1.0" ?>'

    feedstring = header+feedstring

    return feedstring


def amz_inventory_feed(amz, products):
    """

    :return:
    :rtype:
    """
    feed = etree.Element('AmazonEnvelope')

    # create header
    header = etree.SubElement(feed, 'Header')
    documentver = etree.SubElement(header, 'DocumentVersion')
    documentver.text = "1.01"
    merchantidentifier = etree.SubElement(header, 'MerchantIdentifier')
    merchantidentifier.text = amz['mid']

    #MessageType
    msgtype = etree.SubElement(feed, 'MessageType')
    msgtype.text = 'Inventory'

    for i, product in enumerate(products):
        msg = etree.SubElement(feed, 'Message')

        msgid = etree.SubElement(msg, 'MessageID')
        msgid.text = str(i)

        optype = etree.SubElement(msg, 'OperationType')
        optype.text = "update"


        inv = etree.SubElement(msg, 'Inventory')

        sku = etree.SubElement(inv, 'SKU')
        sku.text = product['sku']
        qnty = etree.SubElement(inv, 'Quantity')
        qnty.text = str(product['qnty'])
        ffl = etree.SubElement(inv, 'FulfillmentLatency')
        ffl.text = str(product['ffl'])

        # < Quantity > 8 < / Quantity > < FulfillmentLatency > 1 < / FulfillmentLatency > < / Inventory >

    feedstring = etree.tostring(feed)
    feedstring.replace("<AmazonEnvelope>", '<AmazonEnvelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="amzn- envelope.xsd">')
    header = '<?xml version="1.0" ?>'

    feedstring = header+feedstring

    return feedstring


def amz_price_feed(amz, products):
    """

    :return:
    :rtype:
    """
    feed = etree.Element('AmazonEnvelope')

    # create header
    header = etree.SubElement(feed, 'Header')
    documentver = etree.SubElement(header, 'DocumentVersion')
    documentver.text = "1.01"
    merchantidentifier = etree.SubElement(header, 'MerchantIdentifier')
    merchantidentifier.text = amz['mid']

    #MessageType
    msgtype = etree.SubElement(feed, 'MessageType')
    msgtype.text = 'Price'

    for i, product in enumerate(products):
        msg = etree.SubElement(feed, 'Message')

        msgid = etree.SubElement(msg, 'MessageID')
        msgid.text = str(i)

        price = etree.SubElement(msg, 'Price')
        sku = etree.SubElement(price, 'SKU')
        sku.text = product['sku']
        price = etree.SubElement(price, 'StandardPrice', currency="USD")
        price.text = str(product['MSRP'])

    feedstring = etree.tostring(feed)
    feedstring.replace("<AmazonEnvelope>", '<AmazonEnvelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="amzn- envelope.xsd">')
    header = '<?xml version="1.0" ?>'

    feedstring = header+feedstring

    return feedstring


def amz_image_feed(amz, products):
    """

    :return:
    :rtype:
    """
    feed = etree.Element('AmazonEnvelope')

    # create header
    header = etree.SubElement(feed, 'Header')
    documentver = etree.SubElement(header, 'DocumentVersion')
    documentver.text = "1.01"
    merchantidentifier = etree.SubElement(header, 'MerchantIdentifier')
    merchantidentifier.text = amz['mid']

    #MessageType
    msgtype = etree.SubElement(feed, 'MessageType')
    msgtype.text = 'ProductImage'

    for i, product in enumerate(products):
        msg = etree.SubElement(feed, 'Message')

        msgid = etree.SubElement(msg, 'MessageID')
        msgid.text = str(i)

        optype = etree.SubElement(msg, 'OperationType')
        optype.text = "update"

        img = etree.SubElement(msg, 'ProductImage')
        sku = etree.SubElement(img, 'SKU')
        sku.text = product['sku']
        imgtype = etree.SubElement(img, 'ImageType')
        imgtype.text = product['imgtype']
        imgloc = etree.SubElement(img, 'ImageLocation')
        imgloc.text = product['imgloc']

    feedstring = etree.tostring(feed)
    feedstring.replace("<AmazonEnvelope>", '<AmazonEnvelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="amzn- envelope.xsd">')
    header = '<?xml version="1.0" ?>'

    feedstring = header+feedstring

    return feedstring