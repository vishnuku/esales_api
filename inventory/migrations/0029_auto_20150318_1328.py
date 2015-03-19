# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0008_auto_20150313_1037'),
        ('inventory', '0028_auto_20150318_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductChannelOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.ForeignKey(to='integration.Channel')),
                ('product', models.ForeignKey(to='inventory.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='product',
            name='channel',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
