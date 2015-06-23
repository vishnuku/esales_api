# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_filter_logic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='name',
            field=models.CharField(default=b'', unique=True, max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
