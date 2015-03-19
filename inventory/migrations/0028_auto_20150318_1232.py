# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0027_auto_20150318_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='purchase_price',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='retail_price',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
