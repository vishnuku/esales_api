# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_auto_20150310_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channelcategory',
            name='node_path',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
