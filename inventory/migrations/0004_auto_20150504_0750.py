# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20150504_0716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amazonorders',
            name='miscdata',
        ),
        migrations.AddField(
            model_name='productorder',
            name='quantityordered',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
