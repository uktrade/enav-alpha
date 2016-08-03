# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='web_address',
            field=models.URLField(blank=True, null=True),
        ),
    ]