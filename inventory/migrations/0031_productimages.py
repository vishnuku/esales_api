# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0030_product_parent_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'product/images/upload/%Y/%m/%d')),
                ('is_main', models.BooleanField(default=False)),
                ('status', models.SmallIntegerField(default=1, null=True, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('created_by', models.ForeignKey(related_name='created_by_user_productimages', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(related_name='images', default=1, to='inventory.Product')),
                ('updated_by', models.ForeignKey(related_name='updated_by_user_productimages', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_on',),
            },
            bases=(models.Model,),
        ),
    ]
