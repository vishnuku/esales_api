# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0041_auto_20150406_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='name',
            field=models.FileField(max_length=200, upload_to=b'/home/ranjeet/PycharmProjects/esales_api/esales_api/media/csv/%Y-%m-%d', validators=[inventory.models.validate_file_extension]),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='warehousebin',
            unique_together=set([('warehouse', 'name')]),
        ),
    ]
