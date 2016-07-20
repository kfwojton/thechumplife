# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titlea', models.CharField(max_length=3000, null=True, blank=True)),
                ('message', models.TextField(null=True, blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'images/%Y/%m/%d', blank=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2016, 7, 18, 18, 48, 52, 199168))),
                ('google_doc_link', models.CharField(max_length=3000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
