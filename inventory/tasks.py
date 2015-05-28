from celery import shared_task
from inventory.models import ProductOrder

@shared_task
def map_order_product_warehouse(**kwargs):
    """

    :return:
    :rtype:
    """
    if "pid" in kwargs.keys():
        for productorder in ProductOrder.objects.filter(warehousebin=None, product_id=kwargs['pid']):
            productorder.warehousebin_id = kwargs['binid']
            productorder.save()

    for productorder in ProductOrder.objects.filter(warehousebin=None):
        productorder_obj = ProductOrder.objects.filter(product_id=productorder.product).exclude(warehousebin=None).last()
        if productorder_obj:
            productorder.warehousebin = productorder_obj.warehousebin
            productorder.save()

