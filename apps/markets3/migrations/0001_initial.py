# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 10:26
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('_encoded_data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('web_address', models.URLField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('product_category_demand', models.CommaSeparatedIntegerField(blank=True, max_length=500, null=True)),
                ('size', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('product_category_size', models.CommaSeparatedIntegerField(blank=True, max_length=10000, null=True)),
                ('web_traffic_to_site', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('web_traffic_to_bounce', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('fee_pricing_structure', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('payment_terms', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('logistics_structure', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('seller_support_structure', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('translation_services', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('buyers_customer_service', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('merchandising_offer_cost', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('payment_methods', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('listing_languages', ckeditor.fields.RichTextField(blank=True, max_length=500, null=True)),
                ('product_visibility', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('competitor_comparison', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('ukti_terms', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('contact_details', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('shop_analytics', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('customization', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('social_media_integration', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('product_promotion_options', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('feedback_system', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('revenue', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('parent_company_name', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('platform_target_market', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('product_feedback_system', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('seller_application_process', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('subscription_fees', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('registration_fees', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('additional_fees', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('referral_fees', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('prohibited_items', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('logistics_options', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('local_laws', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('platform_signup', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('things_to_consider', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc3', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc4', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc5', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc6', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc7', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc8', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc9', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc10', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc11', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc12', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc13', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc14', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc15', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc16', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc17', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc18', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc19', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc20', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc21', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc22', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc23', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc24', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc25', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc26', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc27', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc28', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('misc29', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('countries_served', models.ManyToManyField(to='markets3.Country')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                           to='markets3.Logo')),
            ],
            options={
                'ordering': ('country',),
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.AddField(
            model_name='market',
            name='product_categories',
            field=models.ManyToManyField(to='markets3.ProductCategory'),
        ),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets3.Region'),
        ),
    ]
