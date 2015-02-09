# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0009_auto_20150208_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='status',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
