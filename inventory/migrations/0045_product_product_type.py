# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0044_auto_20150408_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(blank=True, max_length=5, choices=[(b'1', b'Normal'), (b'2', b'Bundle'), (b'3', b'Variation Parent')]),
            preserve_default=True,
        ),
    ]
