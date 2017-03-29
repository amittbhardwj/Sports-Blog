# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_t'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t',
            name='follows',
            field=models.ManyToManyField(related_name='follows', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
