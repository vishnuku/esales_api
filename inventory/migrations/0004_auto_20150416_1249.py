# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20150416_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonorders',
            name='address',
            field=json_field.fields.JSONField(default='null', help_text='Enter a valid JSON object'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='misc_data',
            field=json_field.fields.JSONField(default='null', help_text='Enter a valid JSON object'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='warehouse',
            field=json_field.fields.JSONField(default='null', help_text='Enter a valid JSON object'),
            preserve_default=True,
        ),
    ]
