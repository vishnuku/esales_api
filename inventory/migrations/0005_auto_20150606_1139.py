# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0004_auto_20150606_0725'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.IntegerField()),
                ('inventory', models.IntegerField()),
                ('amazonorders', models.IntegerField()),
                ('warehousebin', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StockOut',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.IntegerField()),
                ('inventory', models.IntegerField()),
                ('amazonorders', models.IntegerField()),
                ('warehousebin', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='inventory',
            field=models.ForeignKey(related_name='product_inventory', default=1, to='inventory.Inventory'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='csv',
            name='name',
            field=models.FileField(max_length=200, upload_to=b'/Users/vishnu/PycharmProjects/esales_api/esales_api/media/csv/%Y-%m-%d', validators=[inventory.models.validate_file_extension]),
            preserve_default=True,
        ),
    ]
