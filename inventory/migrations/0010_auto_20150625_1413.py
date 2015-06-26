# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20150612_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inventory',
            field=models.ForeignKey(related_name='product_inventory', blank=True, to='inventory.Inventory', null=True),
            preserve_default=True,
        ),
    ]
