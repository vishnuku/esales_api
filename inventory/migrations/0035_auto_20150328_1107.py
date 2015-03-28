# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0034_warehousebin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehousebin',
            name='product',
            field=models.ForeignKey(blank=True, to='inventory.Product', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='warehousebin',
            name='warehouse',
            field=models.ForeignKey(to='inventory.Warehouse'),
            preserve_default=True,
        ),
    ]
