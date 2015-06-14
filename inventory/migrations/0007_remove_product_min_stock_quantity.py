# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20150609_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='min_stock_quantity',
        ),
    ]
