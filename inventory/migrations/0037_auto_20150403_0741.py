# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0036_productorder_warehousebin'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productorder',
            unique_together=set([('product', 'amazonorders')]),
        ),
    ]
