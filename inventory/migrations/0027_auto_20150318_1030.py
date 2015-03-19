# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0008_auto_20150313_1037'),
        ('inventory', '0026_amazonorders_amazonproduct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='csv',
            options={'ordering': ('created_on',)},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ('created_on',)},
        ),
        migrations.RenameField(
            model_name='amazonorders',
            old_name='created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='amazonorders',
            old_name='updated',
            new_name='updated_on',
        ),
        migrations.RenameField(
            model_name='amazonproduct',
            old_name='created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='amazonproduct',
            old_name='updated',
            new_name='updated_on',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='updated',
            new_name='updated_on',
        ),
        migrations.RenameField(
            model_name='channelcategory',
            old_name='created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='channelcategory',
            old_name='updated',
            new_name='updated_on',
        ),
        migrations.RenameField(
            model_name='csv',
            old_name='created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='csv',
            old_name='updated',
            new_name='updated_on',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='updated',
            new_name='updated_on',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='minimum_stock_level',
            new_name='min_stock_quantity',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='pending_quantity',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='updated',
            new_name='updated_on',
        ),
        migrations.RenameField(
            model_name='productlistingconfigurator',
            old_name='created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='productlistingconfigurator',
            old_name='updated',
            new_name='updated_on',
        ),
        migrations.RenameField(
            model_name='sync',
            old_name='created',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='sync',
            old_name='updated',
            new_name='updated_on',
        ),
        migrations.AddField(
            model_name='product',
            name='channel',
            field=models.ForeignKey(default=1, to='integration.Channel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='expedited_shipping',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='field1',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='field10',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='field2',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='field3',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='field4',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='field5',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='field6',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='field7',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='field8',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='field9',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='misc_data',
            field=json_field.fields.JSONField(default='null', help_text='Enter a valid JSON object'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_fee',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='sold_quantity',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='stock_quantity',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='will_ship_internationally',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='ucodetype',
            field=models.CharField(blank=True, max_length=20, choices=[(b'ISBN', b'ISBN'), (b'UPC', b'UPC'), (b'EAN', b'EAN')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='ucodevalue',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
