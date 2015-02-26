# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20150226_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(default=datetime.datetime(2015, 2, 26, 12, 38, 56, 650234, tzinfo=utc), max_length=255, blank=True),
            preserve_default=False,
        ),
    ]
