# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20150226_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=255, choices=[(b'ISBN', b'ISBN'), (b'UPC', b'UPC'), (b'EAN', b'EAN')]),
            preserve_default=True,
        ),
    ]
