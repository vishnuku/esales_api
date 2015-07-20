# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0023_auto_20150718_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping_setting',
            name='hashcode_data',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
