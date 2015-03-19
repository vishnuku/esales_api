# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0029_auto_20150318_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('status', models.CharField(default=b'', max_length=20, blank=True)),
                ('message', models.CharField(default=b'', max_length=50, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('AmazonOrders', models.ForeignKey(to='inventory.AmazonOrders')),
                ('created_by', models.ForeignKey(related_name='created_by_product_order', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(to='inventory.Product')),
                ('updated_by', models.ForeignKey(related_name='updated_by_product_order', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='productchannelorder',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='productchannelorder',
            name='product',
        ),
        migrations.DeleteModel(
            name='ProductChannelOrder',
        ),
    ]
