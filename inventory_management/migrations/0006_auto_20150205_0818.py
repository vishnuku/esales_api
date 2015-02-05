# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0005_auto_20150205_0629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcategory',
            old_name='user',
            new_name='user_id',
        ),
    ]
