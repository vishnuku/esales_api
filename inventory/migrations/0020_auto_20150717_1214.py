# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_auto_20150717_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_inventory',
            old_name='bin',
            new_name='warehouseBin',
        ),
    ]
