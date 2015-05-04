# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20150429_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazonorders',
            name='miscdata',
            field=jsonfield.fields.JSONField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='csv',
            name='name',
            field=models.FileField(max_length=200, upload_to=b'/Users/vishnu/PycharmProjects/esales_api/esales_api/media/csv/%Y-%m-%d', validators=[inventory.models.validate_file_extension]),
            preserve_default=True,
        ),
    ]
