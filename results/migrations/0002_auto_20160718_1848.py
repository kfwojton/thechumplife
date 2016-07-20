# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 18, 18, 48, 56, 398232)),
            preserve_default=True,
        ),
    ]
