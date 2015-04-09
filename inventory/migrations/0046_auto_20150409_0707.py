# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0045_product_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(default=1, max_length=5, blank=True, choices=[(b'1', b'Normal'), (b'2', b'Bundle'), (b'3', b'Variation Parent')]),
            preserve_default=True,
        ),
    ]
