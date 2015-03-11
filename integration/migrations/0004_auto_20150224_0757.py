# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('integration', '0003_amazoncategories'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazoncategories',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 24, 7, 57, 9, 245794, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amazoncategories',
            name='created_by',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amazoncategories',
            name='node_id',
            field=models.BigIntegerField(),
            preserve_default=True,
        ),
    ]
