# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0039_auto_20150406_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='product',
            field=models.ForeignKey(related_name='productorder', to='inventory.Product'),
            preserve_default=True,
        ),
    ]
