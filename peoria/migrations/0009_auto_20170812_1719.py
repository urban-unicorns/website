# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-12 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoria', '0008_auto_20170812_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gripe',
            name='location',
        ),
        migrations.AddField(
            model_name='gripe',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='gripe',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=40.703545, max_digits=10),
        ),
        migrations.AddField(
            model_name='gripe',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=-89.579086, max_digits=10),
        ),
        migrations.AlterField(
            model_name='project',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=40.703545, max_digits=10),
        ),
        migrations.AlterField(
            model_name='project',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=-89.579086, max_digits=10),
        ),
    ]
