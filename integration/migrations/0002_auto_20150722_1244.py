# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='marketplace',
            field=models.PositiveSmallIntegerField(default=1, choices=[(1, b'Amazon'), (2, b'ebay'), (3, b'Manual'), (4, b'mkt2')]),
            preserve_default=True,
        ),
    ]
