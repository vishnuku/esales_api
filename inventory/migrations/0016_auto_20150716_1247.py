# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0015_remove_product_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.AddField(
            model_name='product',
            name='linked_product',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='csv',
            name='name',
            field=models.FileField(max_length=200, upload_to=b'/home/ranjeet/PycharmProjects/esales_api/esales_api/media/csv/%Y-%m-%d', validators=[inventory.models.validate_file_extension]),
            preserve_default=True,
        ),
    ]
