# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0031_productimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimages',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='productimages',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='productimages',
            name='user',
        ),
    ]
