# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_auto_20150716_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='linked_product',
            new_name='linked_inventory',
        ),
    ]
