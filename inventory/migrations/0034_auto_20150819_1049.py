# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0033_auto_20150813_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_inventory',
            name='inventory',
            field=models.ForeignKey(related_name='product_i_inventory', blank=True, to='inventory.Inventory', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product_inventory',
            name='warehouseBin',
            field=models.ForeignKey(related_name='product_bin', blank=True, to='inventory.WarehouseBin', null=True),
            preserve_default=True,
        ),
    ]
