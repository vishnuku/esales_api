# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0032_auto_20150326_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouseproduct',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='warehouseproduct',
            name='product',
        ),
        migrations.RemoveField(
            model_name='warehouseproduct',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='warehouseproduct',
            name='user',
        ),
        migrations.RemoveField(
            model_name='warehouseproduct',
            name='warehouse',
        ),
        migrations.DeleteModel(
            name='WarehouseProduct',
        ),
        migrations.AddField(
            model_name='product',
            name='warehouse',
            field=json_field.fields.JSONField(default='null', help_text='Enter a valid JSON object'),
            preserve_default=True,
        ),
    ]
