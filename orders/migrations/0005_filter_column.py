# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20150504_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='column',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
