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
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=105)),
                ('address', models.CharField(max_length=105)),
                ('city', models.CharField(max_length=105)),
                ('company', models.CharField(max_length=105)),
                ('country', models.CharField(max_length=105)),
                ('email', models.CharField(max_length=105)),
                ('full_name', models.CharField(max_length=105)),
                ('phone', models.CharField(max_length=105)),
                ('postal', models.CharField(max_length=105)),
                ('state', models.CharField(max_length=105)),
                ('vendor', models.CharField(default=1, max_length=10, choices=[(b'USPS', b'USPS')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
