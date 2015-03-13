# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0006_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amazoncategories',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='AmazonCategories',
        ),
    ]
