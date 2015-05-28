from celery import shared_task
from inventory.models import ProductOrder

@shared_task
def map_order_product_warehouse():
    """

    :return:
    :rtype:
    """
    for productorder in ProductOrder.objects.filter(warehousebin=None):
        productorder_obj = ProductOrder.objects.filter(product_id=productorder.product).exclude(warehousebin=None).last()
        if productorder_obj:
            productorder.warehousebin = productorder_obj.warehousebin
            productorder.save()
            print 'Updated',productorder.id

