# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20150514_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='name',
            field=models.FileField(max_length=200, upload_to=b'/Users/vishnu/PycharmProjects/esales_api/esales_api/media/csv/%Y-%m-%d', validators=[inventory.models.validate_file_extension]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pending_quantity',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='sold_quantity',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
