# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0031_auto_20150326_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='address',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='country',
            field=models.CharField(max_length=105, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='town',
            field=models.CharField(max_length=105, blank=True),
            preserve_default=True,
        ),
    ]
