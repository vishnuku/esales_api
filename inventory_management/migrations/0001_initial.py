# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import inventory_management.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryProductImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=inventory_management.models.get_unique_image_file_path)),
                ('is_main', models.BooleanField(default=0)),
                ('status', models.SmallIntegerField(default=1, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InventoryProducts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_sku', models.CharField(unique=True, max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('purchase_price', models.FloatField()),
                ('retail_price', models.FloatField()),
                ('tax_price', models.FloatField(default=0, blank=True)),
                ('meta_data', models.TextField()),
                ('category_id', models.IntegerField()),
                ('barcode', models.CharField(max_length=200)),
                ('stock_value', models.IntegerField(default=0)),
                ('minimum_stock_level', models.IntegerField(default=0)),
                ('user_id', models.IntegerField()),
                ('status', models.SmallIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(unique=True, max_length=100)),
                ('status', models.SmallIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        )

    ]
