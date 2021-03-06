# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_additional'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moreinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote', models.CharField(max_length=50, blank=True)),
                ('url', models.CharField(max_length=50, blank=True)),
                ('about', models.CharField(max_length=150, blank=True)),
                ('image', models.ImageField(upload_to=b'uploads/', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
