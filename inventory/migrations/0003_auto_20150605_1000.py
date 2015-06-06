# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20150605_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='product',
        ),
        migrations.AddField(
            model_name='images',
            name='inventory',
            field=models.ForeignKey(related_name='images', default=1, to='inventory.Inventory'),
            preserve_default=True,
        ),
    ]
