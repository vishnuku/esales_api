# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channel_integration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amazon',
            old_name='aceess_key',
            new_name='access_key',
        ),
        migrations.RenameField(
            model_name='channelintegration',
            old_name='aceess_key',
            new_name='access_key',
        ),
    ]
