# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150319_0515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addons',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=50, blank=True)),
                ('about', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to=b'uploads/', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='image',
            field=models.ImageField(upload_to=b'uploads/', blank=True),
            preserve_default=True,
        ),
    ]
