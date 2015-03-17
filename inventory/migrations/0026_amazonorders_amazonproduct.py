# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0025_auto_20150313_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazonorders',
            name='amazonproduct',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
