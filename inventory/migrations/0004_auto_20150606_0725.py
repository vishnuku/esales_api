# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20150605_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehousebin',
            name='product',
        ),
        migrations.AddField(
            model_name='warehousebin',
            name='inventory',
            field=models.ForeignKey(related_name='productwarehousebin', blank=True, to='inventory.Inventory', null=True),
            preserve_default=True,
        ),
    ]
