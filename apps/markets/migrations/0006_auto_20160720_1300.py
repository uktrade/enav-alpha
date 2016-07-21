# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0005_auto_20160718_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('_encoded_data', models.TextField()),
            ],
        ),
        migrations.RemoveField(model_name='market', name='logo'),
        migrations.AddField(
            model_name='market',
            name='logo',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='markets.Logo'),
            preserve_default=True)
    ]
