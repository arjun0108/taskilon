# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-11 20:52
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40, verbose_name='Task Name')),
                ('description', models.CharField(default='', max_length=240, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('expire', models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 12, 2, 22, 44, 217475), null=True, verbose_name='Ending On')),
                ('status', models.BooleanField(default=False, verbose_name='Task Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_todo_list', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Task',
            },
        ),
    ]