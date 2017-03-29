# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_moreinfo_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='moreinfo',
            name='quote',
            field=models.CharField(max_length=150, blank=True),
            preserve_default=True,
        ),
    ]
