# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InstaWorkApi', '0004_remove_teammembers_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammembers',
            name='role',
            field=models.CharField(choices=[('AD', 'admin'), ('RE', 'regular')], default='RE', max_length=2),
        ),
    ]
