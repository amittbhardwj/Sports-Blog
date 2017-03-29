# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
        ('blog', '0008_auto_20150321_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additional',
            name='user',
        ),
        migrations.DeleteModel(
            name='Additional',
        ),
        migrations.DeleteModel(
            name='Addons',
        ),
        migrations.RemoveField(
            model_name='extendeduser',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='ExtendedUser',
        ),
    ]
