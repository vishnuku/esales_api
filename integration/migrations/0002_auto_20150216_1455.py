# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='created_by',
            field=models.ForeignKey(related_name='created_by_user_channel', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='channel',
            name='marketplace',
            field=models.PositiveSmallIntegerField(default=1, choices=[(1, b'Amazon'), (2, b'ebay'), (3, b'mkt1'), (4, b'mkt2')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='channel',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_by_user_channel', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='channel',
            name='user_id',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
