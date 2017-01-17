# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=255)),
                ('description', models.TextField()),
                ('size', models.CharField(blank=True, default='', max_length=255)),
                ('rent', models.IntegerField()),
                ('date_available', models.DateField()),
                ('bathroom', models.CharField(blank=True, default='', max_length=255)),
                ('laundry', models.CharField(blank=True, default='', max_length=255)),
                ('pets', models.CharField(blank=True, default='', max_length=255)),
                ('location', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
    ]
