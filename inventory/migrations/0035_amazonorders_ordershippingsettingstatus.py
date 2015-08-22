# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0034_auto_20150819_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazonorders',
            name='ordershippingsettingstatus',
            field=models.SmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
