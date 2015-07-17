# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0020_auto_20150717_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping_Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hashcode', models.IntegerField()),
                ('weight1', models.IntegerField()),
                ('weight1_unit', models.CharField(default=b'', max_length=50, blank=True)),
                ('weight2', models.IntegerField()),
                ('weight2_unit', models.CharField(default=b'', max_length=50, blank=True)),
                ('length', models.FloatField()),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('dimension_unit', models.CharField(default=b'', max_length=50, blank=True)),
                ('d_standard', models.CharField(default=b'', max_length=50, blank=True)),
                ('d_expedited', models.CharField(default=b'', max_length=50, blank=True)),
                ('d_second_day', models.CharField(default=b'', max_length=50, blank=True)),
                ('d_single_day', models.CharField(default=b'', max_length=50, blank=True)),
                ('d_economy', models.CharField(default=b'', max_length=50, blank=True)),
                ('i_standard', models.CharField(default=b'', max_length=50, blank=True)),
                ('i_expedited', models.CharField(default=b'', max_length=50, blank=True)),
                ('i_economy', models.CharField(default=b'', max_length=50, blank=True)),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='csv',
            name='name',
            field=models.FileField(max_length=200, upload_to=b'/Users/vishnu/PycharmProjects/esales_api/esales_api/media/csv/%Y-%m-%d', validators=[inventory.models.validate_file_extension]),
            preserve_default=True,
        ),
    ]
