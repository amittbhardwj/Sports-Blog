# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150321_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moreinfo',
            name='quote',
            field=models.CharField(max_length=150, blank=True),
            preserve_default=True,
        ),
    ]
