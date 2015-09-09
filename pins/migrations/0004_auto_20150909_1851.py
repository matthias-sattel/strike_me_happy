# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0003_pin_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
