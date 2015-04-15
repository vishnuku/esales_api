# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0049_auto_20150415_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonorders',
            name='address',
            field=json_field.fields.JSONField(default='null', help_text='Enter a valid JSON object', null=True, blank=True),
            preserve_default=True,
        ),
    ]
