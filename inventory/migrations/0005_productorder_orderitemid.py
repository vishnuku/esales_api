# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20150504_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='orderitemid',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
