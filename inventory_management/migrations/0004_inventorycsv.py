# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0003_auto_20150213_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryCSV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('csv_name', models.FileField(upload_to=b'/home/ranjeet/PycharmProjects/esales_api/esales_api/media/csv/%Y/%m/%d')),
                ('status', models.SmallIntegerField(default=0)),
                ('user_id', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
    ]
