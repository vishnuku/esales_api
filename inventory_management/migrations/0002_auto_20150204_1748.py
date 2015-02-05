# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_category',
            name='category_name',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
