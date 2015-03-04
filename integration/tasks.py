from __future__ import absolute_import

from boto.mws.connection import MWSConnection
from celery import shared_task
from .models import Channel
from inventory.models import AmazonProduct, Product, Category


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
        # amazon_get_report.apply_async((amz, rid))
        amazon_get_report_vish.apply_async((amz, rid))
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
                                               defaults={'user_id': amz['uid'], 'created_by_id': amz['uid'],
                                                         'updated_by_id': amz['uid']})
        # chek if product is in local inventory
        price = 0
        barcode = 0
        print amz['uid']
        p, created = Product.objects.get_or_create(sku=row[3], defaults={'name': row[0], 'retail_price': row[4],
                                                                         'user_id': amz['uid'].id,
                                                                         'created_by_id': amz['uid'].id,
                                                                         'updated_by_id': amz['uid'].id,
                                                                         'purchase_price': price, 'retail_price': price,
                                                                         'tax_price': price, 'sku': row[3],
                                                                         'barcode': barcode, 'stock': price,
                                                                         'minimum_stock_level': price,
                                                                         'meta_data': price,
                                                                         'category_id': c.id})

        d = AmazonProduct(item_name=row[0], item_description=row[1], listing_id=row[2], seller_sku=row[3],
                          price=row[4], quantity=row[5], open_date=row[6], image_url=row[7],
                          item_is_marketplace=row[8], product_id_type=row[9], zshop_shipping_fee=row[10],
                          item_note=row[11], item_condition=row[12], zshop_category1=row[13],
                          zshop_browse_path=row[14], zshop_storefront_feature=row[15], asin1=row[16], asin2=row[17],
                          asin3=row[18], will_ship_internationally=row[19], expedited_shipping=row[20],
                          zshop_boldface=row[21], bid_for_featured_placement=row[23],
                          add_delete=row[24], pending_quantity=row[25], fulfillment_channel=row[26],
                          channel_id=amz['cid'], product=p,
                          user_id=amz['uid'], created_by_id=amz['uid'].id, updated_by_id=amz['uid'].id)
        dir(d)
        type(d)
        d.save()

        # Update status to completed in ChannelIntegration
        channel = Channel.objects.get(pk=amz['cid'])
        channel.sync_status = 1
        channel.save()

    return True


'''
Below methods are not used
TODO: Remove if required

'''


@shared_task
def amazon_get_report_vish(amz, rid):
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


@shared_task
def amazon_add_product(amz, products):
    """

    :param amz:
    :type amz:
    :param products:
    :type products:
    :return:
    :rtype:
    """

    pass
    con = MWSConnection(aws_access_key_id=amz['akey'], aws_secret_access_key=amz['skey'], Merchant=amz['mid'])
    # rr = con.request_report(ReportType=rtype)
    # rid = rr.RequestReportResult.ReportRequestInfo.ReportRequestId

@shared_task
def amazon_update_product(amz, products):
    pass

@shared_task
def amazon_delete_product():
    pass