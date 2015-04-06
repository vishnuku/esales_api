# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0038_auto_20150406_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='product',
            field=models.ForeignKey(related_name='products', to='inventory.Product'),
            preserve_default=True,
        ),
    ]
