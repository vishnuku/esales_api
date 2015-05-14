# coding=utf-8
from boto.mws.connection import MWSConnection
from lxml import etree


def amz_product_feed(amz, products):
    """

    :param amz:
    :type amz:
    :param products:
    :type products:
    :return:
    :rtype:
    """
    feed = etree.Element('AmazonEnvelope')

    header = etree.SubElement(feed, 'Header')
    documentver = etree.SubElement(header, 'DocumentVersion')
    documentver.text = "1.01"
    merchantidentifier = etree.SubElement(header, 'MerchantIdentifier')
    merchantidentifier.text = amz['mid']

    msgtype = etree.SubElement(feed, 'MessageType')
    msgtype.text = 'Product'

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

    :param amz:
    :type amz:
    :param products:
    :type products:
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

    :param amz:
    :type amz:
    :param products:
    :type products:
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

    :param amz:
    :type amz:
    :param products:
    :type products:
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


def amz_relationship_feed(amz, type, parent_sku, child_skus):
    """

    :param amz:
    :type amz:
    :param type:
    :type type:
    :param parent_sku:
    :type parent_sku:
    :param child_skus:
    :type child_skus:
    :return:
    :rtype:
    """

    RTYPE = {
        '0': 'Variation',
        '1': 'Accessory',
    }

    feed = etree.Element('AmazonEnvelope')

    # create header
    header = etree.SubElement(feed, 'Header')
    documentver = etree.SubElement(header, 'DocumentVersion')
    documentver.text = "1.01"
    merchantidentifier = etree.SubElement(header, 'MerchantIdentifier')
    merchantidentifier.text = amz['mid']

    #MessageType
    msgtype = etree.SubElement(feed, 'MessageType')
    msgtype.text = 'Relationship'

    msg = etree.SubElement(feed, 'Message')

    msgid = etree.SubElement(msg, 'MessageID')
    msgid.text = '1'

    optype = etree.SubElement(msg, 'OperationType')
    optype.text = "Update"

    relationship = etree.SubElement(msg, 'Relationship')
    parentsku = etree.SubElement(relationship, 'ParentSKU')
    parentsku.text = str(parent_sku)

    for child_sku in child_skus:
        relation = etree.SubElement(relationship, 'Relation')
        c_sku = etree.SubElement(relation, 'SKU')
        c_sku.text = str(child_sku)

        c_type = etree.SubElement(relation, 'Type')
        c_type.text = str(RTYPE[str(type)])

    feedstring = etree.tostring(feed)
    feedstring.replace("<AmazonEnvelope>", '<AmazonEnvelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="amzn- envelope.xsd">')
    header = '<?xml version="1.0" ?>'

    return header+feedstring


def amz_shipping_feed(amz, products):
    feed = etree.Element('AmazonEnvelope')

    # create header
    header = etree.SubElement(feed, 'Header')
    documentver = etree.SubElement(header, 'DocumentVersion')
    documentver.text = "1.01"
    merchantidentifier = etree.SubElement(header, 'MerchantIdentifier')
    merchantidentifier.text = amz['mid']

    # MessageType
    msgtype = etree.SubElement(feed, 'MessageType')
    msgtype.text = 'OrderFulfillment'

    for i, product in enumerate(products):
        msg = etree.SubElement(feed, 'Message')

        msgid = etree.SubElement(msg, 'MessageID')
        msgid.text = str(i)

        orderfulfillment = etree.SubElement(msg, 'OrderFulfillment')
        amzorderid = etree.SubElement(orderfulfillment, 'AmazonOrderID')
        amzorderid.text(product['amzorderid'])
        mfid = etree.SubElement(orderfulfillment, 'MerchantFulfillmentID')
        mfid.text(product['mfid'])
        ffdate = etree.SubElement(orderfulfillment, 'FulfillmentDate')
        ffdate.text(product['ffdate'])

        ffdata = etree.SubElement(orderfulfillment, 'FulfillmentData')
        if 'ccode' in product.keys():
            ccode = etree.SubElement(ffdata, 'CarrierCode')
            ccode.text(product['ccode'])
        if 'cname' in product.keys():
            cname = etree.SubElement(ffdata, 'CarrierCode')
            cname.text(product['cname'])
        shipmethod = etree.SubElement(ffdata, 'ShippingMethod')
        shipmethod.text(product['shipmethod'])
        shiptracking = etree.SubElement(ffdata, 'ShipperTrackingNumber')
        shiptracking.text(product['shiptracking'])

        item = etree.SubElement(orderfulfillment, 'Item')
        itemcode = etree.SubElement(item, 'AmazonOrderItemCode')
        itemcode.text(product['itemcode'])
        if 'mfid' in product.keys():
            mfid = etree.SubElement(item, 'MerchantFulfillmentID')
            mfid.text(product['mffid'])
        quantity = etree.SubElement(item, 'Quantity')
        quantity.text(product['quantity'])

    feedstring = etree.tostring(feed)
    feedstring.replace("<AmazonEnvelope>",
                       '<AmazonEnvelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="amzn- envelope.xsd">')
    header = '<?xml version="1.0" ?>'
    feedstring = header + feedstring
    return feedstring


def amz_acknowledge_feed(amz, data):
    pass


def amz_adjustment_feed(amz, data):
    pass


def get_mws_conn(amz):
    """

    :param amz:
    :type amz:
    :return:
    :rtype:
    """

    return MWSConnection(aws_access_key_id=amz['akey'], aws_secret_access_key=amz['skey'], Merchant=amz['mid'])