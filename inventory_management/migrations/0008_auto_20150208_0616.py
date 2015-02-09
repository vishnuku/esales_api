# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0007_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category',
            new_name='category_id',
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='status',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
