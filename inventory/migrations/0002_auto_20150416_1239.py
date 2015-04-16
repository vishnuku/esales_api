# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonorders',
            name='address',
            field=jsonfield.fields.JSONField(null=True),
            preserve_default=True,
        ),
    ]
