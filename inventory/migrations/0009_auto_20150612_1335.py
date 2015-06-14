# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_product_min_stock_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_bundle',
            name='item',
            field=models.ForeignKey(related_name='item_inventory', to='inventory.Inventory'),
            preserve_default=True,
        ),
    ]
