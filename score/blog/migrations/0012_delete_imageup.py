# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20150321_1118'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Imageup',
        ),
    ]
