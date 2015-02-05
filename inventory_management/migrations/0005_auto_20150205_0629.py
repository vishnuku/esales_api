# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0004_auto_20150204_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='user',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='category_name',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
