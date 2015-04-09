# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0046_auto_20150409_0707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Bundle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.FloatField()),
                ('qty', models.SmallIntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('created_by', models.ForeignKey(related_name='created_by_product_bundle', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(related_name='item_product', to='inventory.Product')),
                ('product', models.ForeignKey(related_name='product_product', to='inventory.Product')),
                ('updated_by', models.ForeignKey(related_name='updated_by_product_bundle', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
