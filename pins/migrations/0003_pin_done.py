# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0002_pin_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='done',
            field=models.BooleanField(default='false'),
        ),
    ]
