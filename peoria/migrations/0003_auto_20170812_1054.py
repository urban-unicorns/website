# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-12 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoria', '0002_auto_20170812_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gripe',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
