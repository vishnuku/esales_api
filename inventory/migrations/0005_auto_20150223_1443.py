# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20150223_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='status',
            field=models.SmallIntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
