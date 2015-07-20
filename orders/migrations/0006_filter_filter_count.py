# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_filter_orders_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='filter_count',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
