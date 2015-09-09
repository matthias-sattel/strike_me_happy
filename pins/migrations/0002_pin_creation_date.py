# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
