# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0011_auto_20150209_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryProductImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(max_length=254, upload_to=b'photos')),
                ('is_main', models.BooleanField(default=False)),
                ('status', models.SmallIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('inventory_product', models.ForeignKey(to='inventory_management.InventoryProducts')),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
    ]
