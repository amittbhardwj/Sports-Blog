# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moreinfo',
            name='quote',
            field=models.CharField(default=True, max_length=150, blank=True),
            preserve_default=True,
        ),
    ]
