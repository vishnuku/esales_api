# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='pending_quantity',
            new_name='item_quantity',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='csv',
            name='name',
            field=models.FileField(max_length=200, upload_to=b'/home/ranjeet/PycharmProjects/esales_api/esales_api/media/csv/%Y-%m-%d', validators=[inventory.models.validate_file_extension]),
            preserve_default=True,
        ),
    ]
