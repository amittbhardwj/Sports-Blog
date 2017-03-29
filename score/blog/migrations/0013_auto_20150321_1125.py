# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_delete_imageup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moreinfo',
            old_name='quote',
            new_name='quot',
        ),
    ]
