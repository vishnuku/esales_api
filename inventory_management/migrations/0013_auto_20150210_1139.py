# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0012_inventoryproductimages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventoryproductimages',
            old_name='inventory_product',
            new_name='inventory_product_id',
        ),
    ]
