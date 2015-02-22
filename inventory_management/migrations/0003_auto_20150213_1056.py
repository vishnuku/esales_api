# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0002_inventoryproductimages_inventory_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryproductimages',
            name='inventory_product',
            field=models.ForeignKey(related_name='images', default=1, to='inventory_management.InventoryProducts'),
            preserve_default=True,
        ),
    ]
