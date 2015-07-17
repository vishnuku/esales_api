# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_auto_20150716_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_inventory',
            name='bin',
            field=models.IntegerField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='warehousebin',
            name='inventory',
            field=models.ForeignKey(related_name='inventorywarehousebin', blank=True, to='inventory.Inventory', null=True),
            preserve_default=True,
        ),
    ]
