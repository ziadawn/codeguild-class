# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 21:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
