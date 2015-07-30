# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0029_auto_20150728_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='parent_product',
            field=models.IntegerField(default=None, null=True),
            preserve_default=True,
        ),
    ]
