# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0035_amazonorders_ordershippingsettingstatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_inventory',
            old_name='warehouseBin',
            new_name='warehousebin',
        ),
    ]
