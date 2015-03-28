# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0033_auto_20150327_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarehouseBin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock_quantity', models.IntegerField(default=0)),
                ('min_stock_quantity', models.IntegerField(default=0)),
                ('sold_quantity', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=105)),
                ('status', models.SmallIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('created_by', models.ForeignKey(related_name='created_by_warehouse_product', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(default=1, to='inventory.Product')),
                ('updated_by', models.ForeignKey(related_name='updated_by_warehouse_product', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('warehouse', models.ForeignKey(default=1, to='inventory.Warehouse')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
