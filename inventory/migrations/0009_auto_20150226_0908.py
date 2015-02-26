# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20150226_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='info',
        ),
        migrations.AddField(
            model_name='product',
            name='bullet_point',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='csv',
            name='csv_name',
            field=models.FileField(max_length=200, upload_to=b'/home/ranjeet/PycharmProjects/esales_api/esales_api/media/csv/%Y-%m-%d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='ucodetype',
            field=models.CharField(blank=True, max_length=255, choices=[(b'ISBN', b'ISBN'), (b'UPC', b'UPC'), (b'EAN', b'EAN')]),
            preserve_default=True,
        ),
    ]
