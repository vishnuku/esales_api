# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings



class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marketplace', models.PositiveSmallIntegerField(default=1, choices=[(1, b'Amazon'), (2, b'ebay'), (3, b'mkt1'), (4, b'mkt2')])),
                ('name', models.CharField(default=b'', max_length=100, blank=True)),
                ('site', models.CharField(default=b'', max_length=100, blank=True)),
                ('merchant_id', models.CharField(default=b'', max_length=100, blank=True)),
                ('marketplace_id', models.CharField(default=b'', max_length=100, blank=True)),
                ('merchant_name', models.CharField(unique=True, max_length=100)),
                ('access_key', models.CharField(default=b'', max_length=100, blank=True)),
                ('secret_key', models.CharField(default=b'', max_length=100, blank=True)),
                ('sync_status', models.SmallIntegerField(default=0, blank=True)),
                ('status', models.BooleanField(default=True, verbose_name='Is Enabled')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('created_by', models.ForeignKey(related_name='created_by_user_channel', default=1, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='updated_by_user_channel', default=1, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
    ]
