# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0027_auto_20150728_1119'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0006_filter_filter_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderShippingDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ship_date', models.DateField(null=True)),
                ('shipping_method', models.CharField(max_length=50, null=True)),
                ('shipping_service', models.CharField(max_length=100, null=True)),
                ('tracking_no', jsonfield.fields.JSONField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('created_by', models.ForeignKey(related_name='created_by_order_shipping_detail', to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(to='inventory.AmazonOrders')),
                ('updated_by', models.ForeignKey(related_name='updated_by_order_shipping_detail', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
