# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0028_auto_20150728_1353'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product_inventory',
            unique_together=set([('product', 'inventory')]),
        ),
        migrations.RemoveField(
            model_name='product_inventory',
            name='bundle',
        ),
    ]
