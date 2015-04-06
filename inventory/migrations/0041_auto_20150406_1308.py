# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0040_auto_20150406_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='amazonorders',
            field=models.ForeignKey(related_name='productorder', to='inventory.AmazonOrders'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productorder',
            name='product',
            field=models.ForeignKey(to='inventory.Product'),
            preserve_default=True,
        ),
    ]
