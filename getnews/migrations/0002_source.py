# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-21 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getnews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('urlsToLogos_small', models.CharField(max_length=1000)),
                ('urlsToLogos_medium', models.CharField(max_length=1000)),
                ('urlsToLogos_large', models.CharField(max_length=1000)),
            ],
        ),
    ]
