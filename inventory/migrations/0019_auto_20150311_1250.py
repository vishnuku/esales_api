# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_auto_20150311_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonorders',
            name='amazonorderid',
            field=models.CharField(max_length=50, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='amazonorders',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='amazonorders',
            name='lastupdatedate',
            field=models.DateTimeField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='amazonorders',
            name='marketplaceid',
            field=models.CharField(max_length=50, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='amazonorders',
            name='ordertype',
            field=models.CharField(max_length=50, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='amazonorders',
            name='purchasedate',
            field=models.DateTimeField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='amazonorders',
            name='saleschannel',
            field=models.CharField(max_length=50, null=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='amazonorders',
            name='updated',
            field=models.DateTimeField(auto_now=True, auto_now_add=True, db_index=True),
            preserve_default=True,
        ),
    ]
