# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_auto_20150717_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_inventory',
            name='bin',
            field=models.ForeignKey(related_name='product_bin', to='inventory.WarehouseBin'),
            preserve_default=True,
        ),
    ]
