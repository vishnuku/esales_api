# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0002_auto_20150204_1748'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='product_category',
            new_name='ProductCategory',
        ),
    ]
