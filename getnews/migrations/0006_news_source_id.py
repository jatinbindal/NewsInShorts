# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-21 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getnews', '0005_auto_20160921_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='source_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
