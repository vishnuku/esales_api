# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_amazonorders_numberofitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amazonorders',
            name='numberofitems',
        ),
        migrations.AlterField(
            model_name='product',
            name='created_by',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_by',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
