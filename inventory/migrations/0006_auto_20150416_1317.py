# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20150416_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonorders',
            name='amazonorderid',
            field=models.CharField(max_length=50, unique=True, null=True, db_index=True),
            preserve_default=True,
        ),
    ]
