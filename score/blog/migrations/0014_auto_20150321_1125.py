# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20150321_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moreinfo',
            old_name='quot',
            new_name='quote',
        ),
    ]
