# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channel_integration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channelintegration',
            name='sync_status',
            field=models.SmallIntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
