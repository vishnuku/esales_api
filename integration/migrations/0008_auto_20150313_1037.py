# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0007_auto_20150312_0726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='user_id',
            new_name='user',
        ),
    ]
