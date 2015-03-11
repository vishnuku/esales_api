# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0017_auto_20150310_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmazonOrders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amazonorderid', models.CharField(max_length=50, null=True)),
                ('buyername', models.CharField(max_length=50, null=True)),
                ('buyeremail', models.EmailField(max_length=75, null=True)),
                ('ordertype', models.CharField(max_length=50, null=True)),
                ('numberofitemsshipped', models.SmallIntegerField(null=True)),
                ('numberofitemsunshipped', models.SmallIntegerField(null=True)),
                ('paymentmethod', models.CharField(max_length=50, null=True)),
                ('orderstatus', models.CharField(max_length=50, null=True)),
                ('saleschannel', models.CharField(max_length=50, null=True)),
                ('amount', models.CharField(max_length=50, null=True)),
                ('marketplaceid', models.CharField(max_length=50, null=True)),
                ('fulfillmentchannel', models.CharField(max_length=50, null=True)),
                ('shipservicelevel', models.CharField(max_length=50, null=True)),
                ('address', json_field.fields.JSONField(default='null', help_text='Enter a valid JSON object')),
                ('purchasedate', models.DateTimeField()),
                ('lastupdatedate', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('created_by', models.ForeignKey(related_name='created_by_amazonorders', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='updated_by_amazonorders', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='amazonproduct',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='sync',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='csv',
            name='csv_name',
            field=models.FileField(max_length=200, upload_to=b'/Users/amit/projects/jkweb/esales_api/esales_api/media/csv/%Y-%m-%d'),
            preserve_default=True,
        ),
    ]
