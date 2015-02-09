# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0008_auto_20150208_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='minimum_stock_level',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='products',
            name='stock_value',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
