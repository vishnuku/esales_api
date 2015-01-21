# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channel_integration', '0002_auto_20150121_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='channelintegration',
            name='sync_status',
            field=models.SmallIntegerField(default=0, max_length=1, blank=True),
            preserve_default=True,
        ),
    ]
