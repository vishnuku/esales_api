# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazonorders',
            name='numberofitems',
            field=models.SmallIntegerField(null=True),
            preserve_default=True,
        ),
    ]
