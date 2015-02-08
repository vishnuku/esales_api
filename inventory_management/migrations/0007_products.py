# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0006_auto_20150205_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_sku', models.CharField(unique=True, max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('purchase_price', models.FloatField()),
                ('retail_price', models.FloatField()),
                ('tax_price', models.FloatField(default=0, blank=True)),
                ('meta_data', models.TextField()),
                ('category', models.IntegerField()),
                ('barcode', models.CharField(max_length=200)),
                ('user_id', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
    ]
