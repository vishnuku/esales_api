# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0013_auto_20150630_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField()),
                ('inventory', models.ForeignKey(related_name='product_i_inventory', to='inventory.Inventory')),
                ('product', models.ForeignKey(related_name='product_i_product', to='inventory.Product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='product_inventory',
            unique_together=set([('product', 'inventory')]),
        ),
    ]
