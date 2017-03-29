# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150321_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moreinfo',
            name='quote',
            field=models.CharField(default=b'I', max_length=150),
            preserve_default=True,
        ),
    ]
