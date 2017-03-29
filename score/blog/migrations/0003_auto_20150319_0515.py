# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('blog', '0002_imageup_profilephoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('url', models.CharField(max_length=50, blank=True)),
                ('about', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to=b'uploads/')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.DeleteModel(
            name='ProfilePhoto',
        ),
    ]
