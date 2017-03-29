# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_postview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moreinfo',
            name='quote',
            field=models.CharField(default=b"I didnt want to tell my favorite quote, so you're seeing this", max_length=50),
            preserve_default=True,
        ),
    ]
