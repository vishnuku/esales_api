# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AmazonProduct',
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
                ('bid_for_featured_placement', models.CharField(default=b'', max_length=100, blank=True)),
                ('add_delete', models.CharField(default=b'', max_length=100, blank=True)),
                ('pending_quantity', models.CharField(default=b'', max_length=100, blank=True)),
                ('fulfillment_channel', models.CharField(default=b'', max_length=100, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('channel', models.ForeignKey(to='integration.Channel')),
                ('created_by', models.ForeignKey(related_name='created_by_user_amzp', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, blank=True)),
                ('status', models.SmallIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('created_by', models.ForeignKey(related_name='created_by_user_category', to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='inventory.Category', null=True)),
                ('updated_by', models.ForeignKey(related_name='updated_by_user_category', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'product/images/upload/%Y/%m/%d')),
                ('is_main', models.BooleanField(default=False)),
                ('status', models.SmallIntegerField(default=1, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('created_by', models.ForeignKey(related_name='created_by_user_images', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('purchase_price', models.FloatField()),
                ('retail_price', models.FloatField()),
                ('tax_price', models.FloatField(default=0, blank=True)),
                ('sku', models.CharField(unique=True, max_length=100)),
                ('barcode', models.CharField(max_length=200)),
                ('stock', models.IntegerField(default=0)),
                ('minimum_stock_level', models.IntegerField(default=0)),
                ('meta_data', models.TextField()),
                ('origin', models.CharField(max_length=55, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('category', models.ForeignKey(to='inventory.Category')),
                ('created_by', models.ForeignKey(related_name='created_by_user_product', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='updated_by_user_product', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sync',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task', models.CharField(max_length=255)),
                ('state', models.PositiveSmallIntegerField()),
                ('status', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('channel', models.ForeignKey(to='integration.Channel')),
                ('created_by', models.ForeignKey(related_name='created_by_user_sync', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='updated_by_user_sync', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='images',
            name='product',
            field=models.ForeignKey(to='inventory.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='images',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_by_user_images', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='images',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='amazonproduct',
            name='product',
            field=models.ForeignKey(to='inventory.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='amazonproduct',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_by_user_amzp', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='amazonproduct',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
