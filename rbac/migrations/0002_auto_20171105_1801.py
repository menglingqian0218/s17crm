# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-05 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name_plural': '权限组表'},
        ),
        migrations.AlterModelOptions(
            name='permission',
            options={'verbose_name_plural': '权限表'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name_plural': '角色表'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name_plural': '用户表'},
        ),
        migrations.AddField(
            model_name='group',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='xx', to='rbac.Group'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.Group', verbose_name='权限组'),
        ),
        migrations.AlterField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='rbac.Permission', verbose_name='具有所有权限'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='roles',
            field=models.ManyToManyField(blank=True, to='rbac.Role', verbose_name='具有所有角色'),
        ),
    ]
