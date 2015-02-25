# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0004_auto_20150224_0757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amazoncategories',
            options={'ordering': ('created',)},
        ),
    ]
