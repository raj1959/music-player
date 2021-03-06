# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-23 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('artist', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=1000)),
                ('playlist', models.ManyToManyField(to='hPlay.Playlist')),
            ],
        ),
    ]
