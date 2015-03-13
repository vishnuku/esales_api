# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0021_auto_20150313_0615'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductListingConfig',
            new_name='ProductListingConfigurator',
        ),
    ]
