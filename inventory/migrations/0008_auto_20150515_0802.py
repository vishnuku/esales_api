# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0001_initial'),
        ('inventory', '0007_auto_20150514_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazonorders',
            name='channel',
            field=models.ForeignKey(related_name='channel_amazonorders', default=1, to='integration.Channel'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='min_stock_quantity',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_quantity',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
