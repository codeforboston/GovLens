# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-04-07 00:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agencies', '0002_increase_name_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='agency',
            name='facebook',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='agency',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='agency',
            name='twitter',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='agency',
            name='website',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='agency',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='agency',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]