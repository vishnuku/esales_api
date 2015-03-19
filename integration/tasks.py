import csv
from datetime import datetime, timedelta

from boto.mws.connection import MWSConnection
from celery import shared_task

from .models import Channel
from inventory.models import AmazonProduct, Product, Category, AmazonOrders


@shared_task
def amazon_request_report(amz, rtype='_GET_MERCHANT_LISTINGS_DATA_'):
    """

    :param amz:
    :type amz:
    :param rtype:
    :rtype rtype:
    :return:
    :rtype:
    """
    con = MWSConnection(aws_access_key_id=amz['akey'], aws_secret_access_key=amz['skey'], Merchant=amz['mid'])
    rr = con.request_report(ReportType=rtype)
    rid = rr.RequestReportResult.ReportRequestInfo.ReportRequestId

    amazon_get_report_list.apply_async((amz, rid, rtype), countdown=60)
    return True

    # amazon_get_report_list.apply_async((amz, 1), countdown=60)
    # return True


@shared_task
def amazon_get_report_list(amz, rid, rtype='_GET_MERCHANT_LISTINGS_DATA_'):
    """

    :param amz:
    :type amz:
    :param rid:
    :type rid:
    :param rtype:
    :type rtype:
    :return:
    :rtype:
    """
    con = MWSConnection(aws_access_key_id=amz['akey'], aws_secret_access_key=amz['skey'], Merchant=amz['mid'])
    rr = con.get_report_request_list(ReportRequestIdList=[rid])

    if rr.GetReportRequestListResult.ReportRequestInfo[0].ReportProcessingStatus == '_DONE_':
        rid = rr.GetReportRequestListResult.ReportRequestInfo[0].GeneratedReportId
        amazon_get_report.apply_async((amz, rid))
        # amazon_get_report_vish.apply_async((amz, rid))
        pass
    elif rr.GetReportRequestListResult.ReportRequestInfo[0].ReportProcessingStatus == '_DONE_NO_DATA_':
        pass
    else:
        # rerun after some time
        amazon_get_report_list.apply_async((amz, rid, rtype), countdown=60)
        pass
    return True

    # amazon_get_report_vish.apply_async((amz, rid))
    # return True


@shared_task
def amazon_get_report(amz, rid, rtype='_GET_MERCHANT_LISTINGS_DATA_'):
    """

    :param amz:
    :type amz:
    :param rid:
    :type rid:
    :return:
    :rtype:
    """
    con = MWSConnection(aws_access_key_id=amz['akey'], aws_secret_access_key=amz['skey'], Merchant=amz['mid'])
    rr = con.get_report(ReportId=rid)

    if rtype == '_GET_MERCHANT_LISTINGS_DATA_':
        inventory_process_report(amz, rr)
    elif rtype == '_GET_ORDERS_DATA_':
        order_process_report(amz, rr)
    else:
        raise Exception('Not Implemented', rtype)


def order_process_report(amz, rr):
    """

    :param amz:
    :type amz:
    :param rr:
    :type rr:
    :return:
    :rtype:
    TODO: Do not have sample data to process the report of order sync
    """
    pass


def inventory_process_report(amz, rr):
    """

    :param amz:
    :type amz:
    :param rr:
    :type rr:
    :return:
    :rtype:
    """

    rr = rr.split("\n")
    print(amz)
    del (rr[0])
    del (rr[len(rr) - 1])

    for r in rr:
        row = r.split("\t")
        print row
        # crete or get category
        c, cr = Category.objects.get_or_create(name=row[13],
                                               defaults={'user': amz['uid'], 'created_by': amz['uid'],
                                                         'updated_by': amz['uid']})

        tmp_misc_data = {}
        tmp_misc_data['add_delete'] = row[24],
        tmp_misc_data['fulfillment_channel'] = row[26],
        tmp_misc_data['bid_for_featured_placement'] = row[23],
        tmp_misc_data['zshop_category1'] = row[13],
        tmp_misc_data['zshop_browse_path'] = row[14],
        tmp_misc_data['zshop_storefront_feature'] = row[15],
        tmp_misc_data['zshop_boldface'] = row[21]


        p, created = Product.objects.get_or_create(sku=row[3],
                                                   defaults={'name': row[0],
                                                             'description': row[1],
                                                             'sku': row[3],
                                                             'retail_price': row[4],
                                                             'stock_quantity': row[5],
                                                             'pending_quantity':row[25],
                                                             'image_url':row[7],
                                                             'shipping_fee':row[10],
                                                             'will_ship_internationally':row[19],
                                                             'expedited_shipping':row[20],
                                                             'category_id':c.id,
                                                             'field1':row[6],
                                                             'field2':row[16],
                                                             'field3':row[17],
                                                             'field4':row[18],
                                                             'field5':row[11],
                                                             'field6':row[12],
                                                             'field7':row[9],
                                                             'field8':row[2],
                                                             'field9':row[8],
                                                             'channel':amz['cid'],
                                                             'created_by':amz['uid'],
                                                             'updated_by':amz['uid'],
                                                             'user':amz['uid'],
                                                             'misc_data':tmp_misc_data
                                                            })

        # d = AmazonProduct(item_name=row[0], item_description=row[1], listing_id=row[2], seller_sku=row[3],
        #                   price=row[4], quantity=row[5], open_date=row[6], image_url=row[7],
        #                   item_is_marketplace=row[8], product_id_type=row[9], zshop_shipping_fee=row[10],
        #                   item_note=row[11], item_condition=row[12], zshop_category1=row[13],
        #                   zshop_browse_path=row[14], zshop_storefront_feature=row[15], asin1=row[16], asin2=row[17],
        #                   asin3=row[18], will_ship_internationally=row[19], expedited_shipping=row[20],
        #                   zshop_boldface=row[21], bid_for_featured_placement=row[23],
        #                   add_delete=row[24], pending_quantity=row[25], fulfillment_channel=row[26],
        #                   channel_id=amz['cid'], product=p,
        #                   user=amz['uid'], created_by=amz['uid'], updated_by=amz['uid'])
        # dir(d)
        # type(d)
        # d.save()

        # Update status to completed in ChannelIntegration
        channel = Channel.objects.get(pk=amz['cid'])
        channel.sync_status = 1
        channel.save()

    return True



@shared_task
def amazon_get_order_live(amz, datefrom=None):
    """

    :param amz:
    :type amz:
    :param datefrom:
    :type datefrom:
    :return:
    :rtype:
    """
    orders = []
    if not datefrom:
        datefrom = (datetime.now().replace(microsecond=0) + timedelta(days=-7)).isoformat()+'Z'

    con = MWSConnection(aws_access_key_id=amz['akey'], aws_secret_access_key=amz['skey'], Merchant=amz['mid'])
    rr = con.list_orders(MarketplaceId=[str(amz["mpid"])], CreatedAfter=datefrom)

    for order in rr.ListOrdersResult.Orders.Order:
        tmp_address = {}
        tmp_order = {}
        if order.ShippingAddress is not None:
            address = order.ShippingAddress
            tmp_address['name'] = address.Name if hasattr(address, 'Name') else ''
            tmp_address['city'] = address.City if hasattr(address, 'City') else ''
            tmp_address['country'] = address.CountryCode if hasattr(address, 'CountryCode') else ''
            tmp_address['state'] = address.StateOrRegion if hasattr(address, 'StateOrRegion') else ''
            tmp_address['add1'] = address.AddressLine1 if hasattr(address, 'AddressLine1') else ''
            tmp_address['postalcode'] = address.PostalCode if hasattr(address, 'PostalCode') else ''
            tmp_address['phone'] = address.Phone if hasattr(address, 'Phone') else ''

        tmp_order['address'] = tmp_address
        tmp_order['buyername'] = order.BuyerName if hasattr(order, 'BuyerName') else ''
        tmp_order['buyeremail'] = order.BuyerEmail if hasattr(order, 'BuyerEmail') else ''
        tmp_order['ordertype'] = order.OrderType if hasattr(order, 'OrderType') else ''
        tmp_order['amazonorderid'] = order.AmazonOrderId if hasattr(order, 'AmazonOrderId') else ''
        tmp_order['purchasedate'] = order.PurchaseDate if hasattr(order, 'PurchaseDate') else ''
        tmp_order['lastupdatedate'] = order.LastUpdateDate if hasattr(order, 'LastUpdateDate') else ''
        tmp_order['numberofitemsshipped'] = order.NumberOfItemsShipped if hasattr(order, 'NumberOfItemsShipped') else ''
        tmp_order['numberofitemsunshipped'] = order.NumberOfItemsUnshipped if hasattr(order,
                                                                                      'NumberOfItemsUnshipped') else ''
        tmp_order['paymentmethod'] = order.PaymentMethod if hasattr(order, 'PaymentMethod') else ''
        tmp_order['orderstatus'] = order.OrderStatus if hasattr(order, 'OrderStatus') else ''
        tmp_order['saleschannel'] = order.SalesChannel if hasattr(order, 'SalesChannel') else ''
        tmp_order['amount'] = order.OrderTotal if hasattr(order, 'OrderTotal') else ''
        tmp_order['marketplaceid'] = order.MarketplaceId if hasattr(order, 'MarketplaceId') else ''
        tmp_order['fulfillmentchannel'] = order.FulfillmentChannel if hasattr(order, 'FulfillmentChannel') else ''
        tmp_order['shipservicelevel'] = order.ShipServiceLevel if hasattr(order, 'ShipServiceLevel') else ''


        t = tmp_order
        try:
            amzorder = AmazonOrders.objects.get(amazonorderid=t['amazonorderid'])
            if str(amzorder.orderstatus) != str(t['orderstatus']):
                amzorder.create_from_dict(t, ('created_by', 'amazonorderid'))
                amzorder.save()
                # orders.append(amzorder)
                amazon_get_order_live_details.apply_async((amz, amzorder.id))
        except AmazonOrders.DoesNotExist:
            amzorder = AmazonOrders()
            amzorder.create_from_dict(t)
            amzorder.user = amz['uid']
            amzorder.created_by = amz['uid']
            amzorder.updated_by = amz['uid']
            amzorder.save()
            amazon_get_order_live_details.apply_async((amz, amzorder.id))

    #Call this task to update product id
    # if len(orders>0):
    #     amazon_get_order_live_details.apply_async((amz, orders), countdown=60)


@shared_task
def amazon_get_order_live_details(amz, orderid):
    order = AmazonOrders.objects.get(pk=orderid)
    con = MWSConnection(aws_access_key_id=amz['akey'], aws_secret_access_key=amz['skey'], Merchant=amz['mid'])
    rr = con.list_order_items(AmazonOrderId=order.amazonorderid)
    # rr.ListOrderItemsResult.OrderItems.OrderItem[0].ASIN
    item_list = []
    for item in rr.ListOrderItemsResult.OrderItems.OrderItem:
        try:
            item_obj = Product.objects.get(sku=item.SellerSKU)
            item_list.append(str(item_obj.id))
        except Product.DoesNotExist:
            print 'From Product.DoesNotExist', item.SellerSKU
            pass

    order.amazonproduct = ",".join(item_list)
    print order
    order.save()



@shared_task
def csv_insert(instance):
    '''

    :param instance:
    :return:
    '''
    f = open(str(instance.csv_name),'rU')
    reader = csv.reader(f)
    header = next(reader)
    error_list = []
    for row in reader:
        try:
            product = Product()
            product.name = row[0]
            product.purchase_price=row[1]
            product.retail_price=row[2]
            product.tax_price=row[3]
            product.sku=row[4]
            product.barcode=row[5]
            product.stock=row[6]
            product.minimum_stock_level=row[7]
            product.meta_data=row[8]
            product.origin=row[9]
            # product.created=row[10]
            # product.updated=row[11]
            product.category_id=row[12]
            # product.created_by_id=row[13]
            # product.updated_by_id=row[14]
            # product.user=row[15]

            product.brand=row[16]
            product.desc=row[17]
            product.manufacturer=row[18]
            product.ucodetype=row[19]
            product.ucodevalue=row[20]
            product.bullet_point=row[21]

            # product.created=now(
            # product.updated=row[11]
            product.created_by=instance.user
            product.updated_by=instance.user
            product.user=instance.user
            product.save()
            print 'Created', product.id
        except Exception as e:
            print(e)
            error_list.append(e[1])
