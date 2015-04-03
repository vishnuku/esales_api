# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0035_auto_20150328_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='warehousebin',
            field=models.ForeignKey(blank=True, to='inventory.WarehouseBin', null=True),
            preserve_default=True,
        ),
    ]
