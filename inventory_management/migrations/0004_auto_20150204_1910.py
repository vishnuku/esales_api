# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0003_auto_20150204_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='category_name',
            field=models.CharField(unique=True, max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
