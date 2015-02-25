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

    amazon_get_report_list.apply_async((amz, rid), countdown=60)
    return True

    # amazon_get_report_list.apply_async((amz, 1), countdown=60)
    # return True


@shared_task
def amazon_get_report_list(amz, rid):
    """

    :param amz:
    :type amz:
    :param rid:
    :type rid:
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
        amazon_get_report_list.apply_async((amz, rid), countdown=60)
        pass
    return True

    # amazon_get_report_vish.apply_async((amz, rid))
    # return True

@shared_task
def amazon_get_report(amz, rid):
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
    rr = rr.split("\n")

    del(rr[0])
    del(rr[len(rr)-1])

    for r in rr:
        row = r.split("\t")
        print row
        #crete or get category
        c, cr = Category.objects.get_or_create(name=row[13], defaults={'user_id': amz['uid'], 'created_by_id': amz['uid'],
                                                                         'updated_by_id': amz['uid']})
        # chek if product is in local inventory
        price = 0
        barcode = 0
        print amz['uid']
        p, created = Product.objects.get_or_create(sku=row[3], defaults={'name': row[0], 'retail_price': row[4],
                                                                         'user_id': amz['uid'].id, 'created_by_id': amz['uid'].id,
                                                                         'updated_by_id': amz['uid'].id,
                                                                         'purchase_price' : price, 'retail_price' : price,
                                                                         'tax_price' : price, 'sku' : row[3],
                                                                         'barcode' : barcode, 'stock' : price,
                                                                         'minimum_stock_level' : price, 'meta_data' : price,
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

        d.save()

        # Update status to completed in ChannelIntegration
        channel = Channel.objects.get(pk=amz['cid'])
        channel.sync_status = 1
        channel.save()

    return True

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
#     rr  = 'item-name	item-description	listing-id	seller-sku	price	quantity	open-date	image-url	item-is-marketplace	product-id-type	zshop-shipping-fee	item-note	item-condition	zshop-category1	zshop-browse-path	zshop-storefront-feature	asin1	asin2	asin3	will-ship-internationally	expedited-shipping	zshop-boldface	product-id	bid-for-featured-placement	add-delete	pending-quantity	fulfillment-channel\n\
# ztech 3 Feet 30 Pin to USB Data Sync Transfer and Charging USB cable Cord for...		0221PM97Y4G	00-5TVO-I6FK	4.3	200	2015-02-21 14:08:24 PST		y	1			11				B00T812EC4			1	N		B00T812EC4			0	DEFAULT\n\
# ztech 3 Feet 30 Pin to USB Data Sync Transfer and Charging USB cable Cord for...		0221PM97Y4G	10-5TVO-I6FK	4.3	200	2015-02-21 14:08:24 PST		y	1			11				B00T812EC4			1	N		B00T812EC4			0	DEFAULT\n\
# ztech 3 Feet 30 Pin to USB Data Sync Transfer and Charging USB cable Cord for...		0221PM97Y4G	10-5TVO-I6FK	4.3	200	2015-02-21 14:08:24 PST		y	1			11				B00T812EC4			1	N		B00T812EC4			0	DEFAULT\n\
# ztech 3 Feet 30 Pin to USB Data Sync Transfer and Charging USB cable Cord for...		0221PM97Y4G	10-5TVO-I6FK	4.3	200	2015-02-21 14:08:24 PST		y	1			11				B00T812EC4			1	N		B00T812EC4			0	DEFAULT\n\
# ztech 3 Feet 30 Pin to USB Data Sync Transfer and Charging USB cable Cord for...		0221PM97W84	17-RUFD-LEAZ	4.3	200	2015-02-21 14:08:18 PST		y	1			11				B00T812D3O			1	N		B00T812D3O			0	DEFAULT'
    rr = rr.split("\n")
    print(amz)
    del(rr[0])
    del(rr[len(rr)-1])

    for r in rr:
        row = r.split("\t")
        print row
        #crete or get category
        c, cr = Category.objects.get_or_create(name=row[13], defaults={'user_id': amz['uid'], 'created_by_id': amz['uid'],
                                                                         'updated_by_id': amz['uid']})
        # chek if product is in local inventory
        price = 0
        barcode = 0
        print amz['uid']
        p, created = Product.objects.get_or_create(sku=row[3], defaults={'name': row[0], 'retail_price': row[4],
                                                                         'user_id': amz['uid'].id, 'created_by_id': amz['uid'].id,
                                                                         'updated_by_id': amz['uid'].id,
                                                                         'purchase_price' : price, 'retail_price' : price,
                                                                         'tax_price' : price, 'sku' : row[3],
                                                                         'barcode' : barcode, 'stock' : price,
                                                                         'minimum_stock_level' : price, 'meta_data' : price,
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