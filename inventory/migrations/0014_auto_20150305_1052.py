# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20150226_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='csv_name',
            field=models.FileField(max_length=200, upload_to=b'/Users/amit/projects/jkweb/esales_api/esales_api/media/csv/%Y-%m-%d'),
            preserve_default=True,
        ),
    ]
