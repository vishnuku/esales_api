# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amazon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, blank=True)),
                ('user', models.CharField(default=b'', max_length=100, blank=True)),
                ('merchant_id', models.CharField(default=b'', max_length=100, blank=True)),
                ('marketplace_id', models.CharField(default=b'', max_length=100, blank=True)),
                ('access_key', models.CharField(default=b'', max_length=100, blank=True)),
                ('secret_key', models.CharField(default=b'', max_length=100, blank=True)),
                ('status', models.BooleanField(default=True, verbose_name='Is Enabled')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AmazonInventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(default=b'', max_length=100, blank=True)),
                ('item_description', models.CharField(default=b'', max_length=100, blank=True)),
                ('listing_id', models.CharField(default=b'', max_length=100, blank=True)),
                ('seller_sku', models.CharField(default=b'', max_length=100, blank=True)),
                ('price', models.CharField(default=b'', max_length=100, blank=True)),
                ('quantity', models.CharField(default=b'', max_length=100, blank=True)),
                ('open_date', models.CharField(default=b'', max_length=100, blank=True)),
                ('image_url', models.CharField(default=b'', max_length=100, blank=True)),
                ('item_is_marketplace', models.CharField(default=b'', max_length=100, blank=True)),
                ('product_id_type', models.CharField(default=b'', max_length=100, blank=True)),
                ('zshop_shipping_fee', models.CharField(default=b'', max_length=100, blank=True)),
                ('item_note', models.CharField(default=b'', max_length=100, blank=True)),
                ('item_condition', models.CharField(default=b'', max_length=100, blank=True)),
                ('zshop_category1', models.CharField(default=b'', max_length=100, blank=True)),
                ('zshop_browse_path', models.CharField(default=b'', max_length=100, blank=True)),
                ('zshop_storefront_feature', models.CharField(default=b'', max_length=100, blank=True)),
                ('asin1', models.CharField(default=b'', max_length=100, blank=True)),
                ('asin2', models.CharField(default=b'', max_length=100, blank=True)),
                ('asin3', models.CharField(default=b'', max_length=100, blank=True)),
                ('will_ship_internationally', models.CharField(default=b'', max_length=100, blank=True)),
                ('expedited_shipping', models.CharField(default=b'', max_length=100, blank=True)),
                ('zshop_boldface', models.CharField(default=b'', max_length=100, blank=True)),
                ('product_id', models.CharField(default=b'', max_length=100, blank=True)),
                ('bid_for_featured_placement', models.CharField(default=b'', max_length=100, blank=True)),
                ('add_delete', models.CharField(default=b'', max_length=100, blank=True)),
                ('pending_quantity', models.CharField(default=b'', max_length=100, blank=True)),
                ('fulfillment_channel', models.CharField(default=b'', max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChannelIntegration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default=b'', max_length=100, blank=True)),
                ('site', models.CharField(default=b'', max_length=100, blank=True)),
                ('merchant_id', models.CharField(default=b'', max_length=100, blank=True)),
                ('marketplace_id', models.CharField(default=b'', max_length=100, blank=True)),
                ('merchant_name', models.CharField(unique=True, max_length=100)),
                ('access_key', models.CharField(default=b'', max_length=100, blank=True)),
                ('secret_key', models.CharField(default=b'', max_length=100, blank=True)),
                ('sync_status', models.SmallIntegerField(default=0, max_length=1, blank=True)),
                ('status', models.BooleanField(default=True, verbose_name='Is Enabled')),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='amazoninventory',
            name='channel',
            field=models.ForeignKey(to='channel_integration.ChannelIntegration'),
            preserve_default=True,
        ),
    ]
