# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_remove_product_min_stock_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='min_stock_quantity',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
