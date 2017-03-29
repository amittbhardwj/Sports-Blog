# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20150321_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moreinfo',
            name='quote',
        ),
    ]
