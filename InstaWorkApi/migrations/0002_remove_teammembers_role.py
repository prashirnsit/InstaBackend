# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 06:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InstaWorkApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammembers',
            name='role',
        ),
    ]