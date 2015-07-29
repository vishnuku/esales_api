# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0027_auto_20150728_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_inventory',
            name='bundle',
            field=models.IntegerField(default=None),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='product_inventory',
            unique_together=set([('product', 'inventory', 'bundle')]),
        ),
    ]
