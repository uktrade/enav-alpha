# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 15:59
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets3', '0005_auto_20160803_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='local_customer_service_notes',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='notes'),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc10',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Website traffic - grey box1', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc11',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Website traffic - grey box2', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc12',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Website traffic - grey box3', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc13',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Website traffic - grey box4', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc14',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Demographic profile', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc15',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Product upload process', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc16',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Customer support', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc17',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Local return address (Yes/No)', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc18',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Return rates', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc19',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Marketing and merchandising', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc20',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Local incorporation', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc21',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Local bank account', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc22',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Exclusivity', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc23',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Translation', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc24',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Payment time', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc25',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Exchange rate', null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='misc26',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Bond required', null=True),
        ),
    ]
