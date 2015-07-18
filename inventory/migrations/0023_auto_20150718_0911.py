# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0022_auto_20150718_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='linked_inventory',
            field=jsonfield.fields.JSONField(null=True),
            preserve_default=True,
        ),
    ]
