from __future__ import absolute_import

from boto.mws.connection import MWSConnection
from celery import shared_task
from .models import AmazonInventory, ChannelIntegration


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
        amazon_get_report.apply_async((amz, rid))
        pass
    elif rr.GetReportRequestListResult.ReportRequestInfo[0].ReportProcessingStatus == '_DONE_NO_DATA_':
        pass
    else:
        # rerun after some time
        amazon_get_report_list.apply_async((amz, rid), countdown=60)
        pass
    return True


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
        d = AmazonInventory(item_name=row[0], item_description=row[1], listing_id=row[2], seller_sku=row[3],
                            price=row[4], quantity=row[5], open_date=row[6], image_url=row[7],
                            item_is_marketplace=row[8], product_id_type=row[9], zshop_shipping_fee=row[10],
                            item_note=row[11], item_condition=row[12], zshop_category1=row[13],
                            zshop_browse_path=row[14], zshop_storefront_feature=row[15], asin1=row[16], asin2=row[17],
                            asin3=row[18], will_ship_internationally=row[19], expedited_shipping=row[20],
                            zshop_boldface=row[21], product_id=row[22], bid_for_featured_placement=row[23],
                            add_delete=row[24], pending_quantity=row[25], fulfillment_channel=row[26],
                            channel_id=amz['cid'])
        d.save()

        # Update status to completed in ChannelIntegration
        channel = ChannelIntegration.objects.get(pk=amz['cid'])
        channel.sync_status = 1
        channel.save()

    return True


@shared_task
def amazon_add_product():
    pass

@shared_task
def amazon_update_product():
    pass

@shared_task
def amazon_delete_product():
    pass