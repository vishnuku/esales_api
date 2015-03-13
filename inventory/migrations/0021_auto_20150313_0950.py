# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0020_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductListingConfigurator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('marketplace', models.CharField(max_length=255)),
                ('marketplace_domain', models.CharField(max_length=255)),
                ('category3', models.CharField(max_length=255)),
                ('status', models.SmallIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('category1', models.ForeignKey(related_name='category1_product_listing_conf', to='inventory.ChannelCategory')),
                ('category2', models.ForeignKey(related_name='category2_product_listing_conf', to='inventory.ChannelCategory')),
                ('created_by', models.ForeignKey(related_name='created_by_product_listing_conf', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='updated_by_product_listing_conf', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='csv',
            name='created_by',
            field=models.ForeignKey(related_name='created_by_csv', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='csv',
            name='name',
            field=models.FileField(default=1, max_length=200, upload_to=b'/Users/vishnu/PycharmProjects/esales_api/esales_api/media/csv/%Y-%m-%d', validators=[inventory.models.validate_file_extension]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='csv',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 13, 9, 50, 26, 696969, tzinfo=utc), auto_now=True, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='csv',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_by_csv', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='csv',
            name='status',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
