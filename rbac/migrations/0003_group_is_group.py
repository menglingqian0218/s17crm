# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-05 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_auto_20171105_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='is_group',
            field=models.BooleanField(default=1, verbose_name='是否是组'),
            preserve_default=False,
        ),
    ]