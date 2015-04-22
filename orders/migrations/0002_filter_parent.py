# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='orders_filter_sub_uom_categories', blank=True, to='orders.Filter', null=True),
            preserve_default=True,
        ),
    ]
