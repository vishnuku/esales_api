# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0021_auto_20150313_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csv',
            name='csv_name',
        ),
        migrations.AlterField(
            model_name='productlistingconfigurator',
            name='created_by',
            field=models.ForeignKey(related_name='created_by_product_listing_conf1', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productlistingconfigurator',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_by_product_listing_conf2', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
