# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 18:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
    ]