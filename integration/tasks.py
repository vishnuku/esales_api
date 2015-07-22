import csv

from datetime import datetime, timedelta
import pickle

from boto.mws.connection import MWSConnection
from celery import shared_task
from django.contrib.auth.models import User
from django.db.models import Q

from integration.models import Channel
from inventory.models import Product, Category, AmazonOrders, ProductOrder
import itertools
from orders.models import Filter


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
        print 'amazon_get_report_list: ', rr.GetReportRequestListResult.ReportRequestInfo[0].ReportProcessingStatus

        rid = rr.GetReportRequestListResult.ReportRequestInfo[0].GeneratedReportId
        amazon_get_report.apply_async((amz, rid, rtype))
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

    print 'amazon_get_report'

    if rtype == '_GET_MERCHANT_LISTINGS_DATA_':
        print 'amazon_get_report: if condition'
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
    rr = rr.split("\n")
    print(amz)
    rh = rr[0].split("\t")
    del (rr[0])
    del (rr[len(rr) - 1])

    for r in rr:
        row = r.split("\t")
        print row
        # crete or get category
        try:
            row_data = dict(itertools.izip_longest(rh, row))
            c, cr = Category.objects.get_or_create(name=row[13],
                                                   defaults={'user': amz['uid'], 'created_by': amz['uid'],
                                                             'updated_by': amz['uid']})

            tmp_misc_data = {}
            tmp_misc_data['add_delete'] = row_data['add-delete'],
            tmp_misc_data['fulfillment_channel'] = row_data['fulfillment-channel'],
            tmp_misc_data['bid_for_featured_placement'] = row_data['bid-for-featured-placement'],
            tmp_misc_data['zshop_category1'] = row_data['zshop-category1'],
            tmp_misc_data['zshop_browse_path'] = row_data['zshop-browse-path'],
            tmp_misc_data['zshop_storefront_feature'] = row_data['zshop-storefront-feature'],
            tmp_misc_data['zshop_boldface'] = row_data['zshop-boldface']

            p, created = Product.objects.get_or_create(sku=row_data['seller-sku'],
                                                       defaults={'name': row_data['item-name'],
                                                                 'description': row_data['item-description'],
                                                                 'sku': row_data['seller-sku'],
                                                                 'retail_price': row_data['price'],
                                                                 'stock_quantity': int(row_data['quantity']) if
                                                                 row_data['quantity'].isdigit() else 0,
                                                                 'pending_quantity': int(
                                                                     row_data['pending-quantity']) if row_data[
                                                                     'pending-quantity'].isdigit() else 0,
                                                                 'image_url': row_data['image-url'],
                                                                 'shipping_fee': row_data['zshop-shipping-fee'] if
                                                                 row_data['zshop-shipping-fee'].isdigit() else 0,
                                                                 'will_ship_internationally': row_data[
                                                                     'will-ship-internationally'],
                                                                 'expedited_shipping': row_data['expedited-shipping'],
                                                                 'category_id': c.id,
                                                                 'field1': row_data['open-date'],
                                                                 'field2': row_data['asin1'],
                                                                 'field3': row_data['asin2'],
                                                                 'field4': row_data['asin3'],
                                                                 'field5': row_data['item-note'],
                                                                 'field6': row_data['item-condition'],
                                                                 'field7': row_data['product-id-type'],
                                                                 'field8': row_data['listing-id'],
                                                                 'field9': row_data['item-is-marketplace'],
                                                                 'channel': amz['cid'],
                                                                 'created_by': amz['uid'].id,
                                                                 'updated_by': amz['uid'].id,
                                                                 'user': amz['uid'],
                                                                 'misc_data': tmp_misc_data
                                                       })
            if not created:
                p.stock_quantity = int(row[5])
                p.save()

            # Update status to completed in ChannelIntegration
            channel = Channel.objects.get(pk=amz['cid'])
            channel.sync_status = 1
            channel.save()
        except Exception as e:
            print 'Exception while product creation', e.message
            print dir(e)

    return True


@shared_task
def amazon_get_order(uid, datefrom=None):
    try:
        ch = Channel.objects.filter(status=1)
        for channel in ch:
            amz = {}
            amz["akey"] = channel.access_key
            amz["skey"] = channel.secret_key
            amz["mid"] = channel.merchant_id
            amz["mpid"] = channel.marketplace_id
            amz["cid"] = channel
            amz["uid"] = uid
            amazon_get_order_live.delay(amz, datefrom)
    except Channel.DoesNotExist:
        pass


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
        datefrom = (datetime.now().replace(microsecond=0) + timedelta(days=-10)).isoformat() + 'Z'

        # Get the latest updatedate from db
        # last_updated_order = AmazonOrders.objects.all().order_by('-lastupdatedate')[:1]
        # if last_updated_order:
        #     datefrom = ((last_updated_order[0].lastupdatedate).replace(tzinfo=None)).isoformat() + 'Z'

    con = MWSConnection(aws_access_key_id=amz['akey'], aws_secret_access_key=amz['skey'], Merchant=amz['mid'])
    # rr = con.list_orders(MarketplaceId=[str(amz["mpid"])], CreatedAfter=datefrom)
    rr = con.list_orders(MarketplaceId=[str(amz["mpid"])], LastUpdatedAfter=datefrom)
    print("before order loop")
    if rr:
        for order in rr.ListOrdersResult.Orders.Order:
            sync_order_to_db(amz, order)

        token = str(rr.ListOrdersResult.NextToken) if hasattr(rr.ListOrdersResult, 'NextToken') else None
        if token:
            print 'First token found', token
            goto_next_token.delay(amz, token)


@shared_task()
def goto_next_token(amz, token):
    con = MWSConnection(aws_access_key_id=amz['akey'], aws_secret_access_key=amz['skey'], Merchant=amz['mid'])
    rt = con.list_orders_by_next_token(MarketplaceId=[str(amz["mpid"])], NextToken=token)
    for order in rt.ListOrdersByNextTokenResult.Orders.Order:
        sync_order_to_db(amz, order)

    token = str(rt.ListOrdersByNextTokenResult.NextToken) if hasattr(rt.ListOrdersByNextTokenResult,
                                                                     'NextToken') else None
    if token:
        print 'Another token found', token
        goto_next_token.delay(amz, token)


def sync_order_to_db(amz, order):
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
            amazon_get_order_live_details.apply_async((amz, amzorder.id, order.OrderStatus))
    except AmazonOrders.DoesNotExist:
        amzorder = AmazonOrders()
        amzorder.create_from_dict(t)
        amzorder.channel = amz['cid']
        amzorder.user = amz['uid']
        amzorder.created_by = amz['uid']
        amzorder.updated_by = amz['uid']
        amzorder.save()
        amazon_get_order_live_details.apply_async((amz, amzorder.id, order.OrderStatus))

        # Call this task to update product id
        # if len(orders>0):
        # amazon_get_order_live_details.apply_async((amz, orders), countdown=60)


@shared_task
def amazon_get_order_live_details(amz, orderid, orderstatus):
    order = AmazonOrders.objects.get(pk=orderid)
    con = MWSConnection(aws_access_key_id=amz['akey'], aws_secret_access_key=amz['skey'], Merchant=amz['mid'])
    rr = con.list_order_items(AmazonOrderId=order.amazonorderid)
    # rr.ListOrderItemsResult.OrderItems.OrderItem[0].ASIN
    item_list = []
    item_obj = 0
    for item in rr.ListOrderItemsResult.OrderItems.OrderItem:
        try:
            # Create order item product if not exitst on our DB
            item_obj, item_created = Product.objects.get_or_create(sku=item.SellerSKU,
                                                                   defaults={'name': item.Title,
                                                                             'sku': item.SellerSKU,
                                                                             'retail_price': item.ItemPrice,
                                                                             'stock_quantity': item.QuantityOrdered,
                                                                             'field2': item.ASIN,
                                                                             'channel': amz['cid'].id,
                                                                             'created_by': amz['uid'].id,
                                                                             'updated_by': amz['uid'].id,
                                                                             'user': amz['uid']
                                                                   })

            item_list.append(str(item_obj.id))

            # Check if same product is already mapped
            # if mapped get latest record
            productorder_obj = ProductOrder.objects.filter(product_id=item_obj.id).last()

            if (item.QuantityShipped > 0):
                item_obj.sold_quantity += int(item.QuantityShipped)
                item_obj.save()

            productorder, created = ProductOrder.objects.get_or_create(product_id=item_obj.id, amazonorders_id=orderid,
                                                                       defaults={'quantity': item.QuantityShipped,
                                                                                 'status': orderstatus,
                                                                                 'orderitemid': item.OrderItemId,
                                                                                 'message': '',
                                                                                 'warehousebin': getattr(
                                                                                     productorder_obj, 'warehousebin',
                                                                                     None),
                                                                                 'user': amz['uid'],
                                                                                 'created_by': amz['uid'],
                                                                                 'updated_by': amz['uid']})

            productorder.save()

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
    f = open(str(instance.csv_name), 'rU')
    reader = csv.reader(f)
    header = next(reader)
    error_list = []
    for row in reader:
        try:
            product = Product()
            product.name = row[0]
            product.purchase_price = row[1]
            product.retail_price = row[2]
            product.tax_price = row[3]
            product.sku = row[4]
            product.barcode = row[5]
            product.stock = row[6]
            product.minimum_stock_level = row[7]
            product.meta_data = row[8]
            product.origin = row[9]
            # product.created=row[10]
            # product.updated=row[11]
            product.category_id = row[12]
            # product.created_by_id=row[13]
            # product.updated_by_id=row[14]
            # product.user=row[15]

            product.brand = row[16]
            product.desc = row[17]
            product.manufacturer = row[18]
            product.ucodetype = row[19]
            product.ucodevalue = row[20]
            product.bullet_point = row[21]

            product.created_by = instance.user
            product.updated_by = instance.user
            product.user = instance.user
            product.save()
            print 'Created', product.id
        except Exception as e:
            print(e)
            error_list.append(e[1])


@shared_task
def sync_inventory():
    channels = Channel.objects.filter(status=1)
    print 'Sync inv'

    for ch in channels:
        amz = {}
        amz["akey"] = ch.access_key
        amz["skey"] = ch.secret_key
        amz["mid"] = ch.merchant_id
        amz["mpid"] = ch.marketplace_id
        amz["cid"] = ch.id
        amz["uid"] = User.objects.get(pk=1)
        amazon_request_report.delay(amz, '_GET_MERCHANT_LISTINGS_DATA_')


@shared_task
def sync_filter_count():
    try:
        filters = Filter.objects.all()
        win_filter = Q(orderstatus__in=['Shipped', 'Unshipped', 'Processing'], fulfillmentchannel='MFN')

        for filter in filters:
            if filter:
                ancestor_logic = Q()  # Create Q object to hold other query
                # If filter is only root node
                if filter.is_root_node():
                    ancestor_logic = pickle.loads(filter.logic)  #Deserilize the filter logic

                #If filter has parents
                else:
                    for filter_data in filter.get_ancestors(False, True):  #Get all parents including self
                        filter_logic = pickle.loads(filter_data.logic)  #Deserilize the filter logic
                        if ancestor_logic.__len__() == 0:
                            ancestor_logic = filter_logic
                        else:
                            ancestor_logic = ancestor_logic & filter_logic

                if ancestor_logic:
                    queryset = AmazonOrders.objects.filter(ancestor_logic & win_filter)  #pass the query object to filter
                    if queryset:
                        f = Filter.objects.get(pk=filter.id)
                        f.filter_count = queryset.count()
                        f.save()

    except Exception as e:
        print e


@shared_task
def sync_order():
    try:
        ch = Channel.objects.filter(status=1, marketplace=1)
        for channel in ch:
            amz = {}
            amz["akey"] = channel.access_key
            amz["skey"] = channel.secret_key
            amz["mid"] = channel.merchant_id
            amz["mpid"] = channel.marketplace_id
            amz["cid"] = channel
            amz["uid"] = User.objects.get(pk=1)
            amazon_get_order_live.delay(amz)
            # print('amz',amz)

        sync_filter_count.delay()
    except Channel.DoesNotExist:
        pass
