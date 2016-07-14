# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='market',
            name='additional_operating_costs',
        ),
        migrations.RemoveField(
            model_name='market',
            name='brand_domestic',
        ),
        migrations.RemoveField(
            model_name='market',
            name='brand_international',
        ),
        migrations.RemoveField(
            model_name='market',
            name='brand_own',
        ),
        migrations.RemoveField(
            model_name='market',
            name='comments_notes',
        ),
        migrations.RemoveField(
            model_name='market',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='market',
            name='contact_address',
        ),
        migrations.RemoveField(
            model_name='market',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='market',
            name='contact_name',
        ),
        migrations.RemoveField(
            model_name='market',
            name='contact_other',
        ),
        migrations.RemoveField(
            model_name='market',
            name='contact_phone',
        ),
        migrations.RemoveField(
            model_name='market',
            name='contact_position',
        ),
        migrations.RemoveField(
            model_name='market',
            name='date_established',
        ),
        migrations.RemoveField(
            model_name='market',
            name='goods_sold',
        ),
        migrations.RemoveField(
            model_name='market',
            name='listing_english',
        ),
        migrations.RemoveField(
            model_name='market',
            name='listing_local',
        ),
        migrations.RemoveField(
            model_name='market',
            name='logistic_diy',
        ),
        migrations.RemoveField(
            model_name='market',
            name='logistic_full',
        ),
        migrations.RemoveField(
            model_name='market',
            name='logistic_partial',
        ),
        migrations.RemoveField(
            model_name='market',
            name='online_marketing',
        ),
        migrations.RemoveField(
            model_name='market',
            name='parent_company_name',
        ),
        migrations.RemoveField(
            model_name='market',
            name='payment_bank_transfer',
        ),
        migrations.RemoveField(
            model_name='market',
            name='payment_cod',
        ),
        migrations.RemoveField(
            model_name='market',
            name='payment_credit_card',
        ),
        migrations.RemoveField(
            model_name='market',
            name='payment_debit_card',
        ),
        migrations.RemoveField(
            model_name='market',
            name='payment_other',
        ),
        migrations.RemoveField(
            model_name='market',
            name='payment_pay_pal',
        ),
        migrations.RemoveField(
            model_name='market',
            name='platform',
        ),
        migrations.RemoveField(
            model_name='market',
            name='position_discount',
        ),
        migrations.RemoveField(
            model_name='market',
            name='position_midpoint',
        ),
        migrations.RemoveField(
            model_name='market',
            name='position_premium',
        ),
        migrations.RemoveField(
            model_name='market',
            name='referral_fee',
        ),
        migrations.RemoveField(
            model_name='market',
            name='registration_fee',
        ),
        migrations.RemoveField(
            model_name='market',
            name='seller_application_process',
        ),
        migrations.RemoveField(
            model_name='market',
            name='shipping_fulfillment_details',
        ),
        migrations.RemoveField(
            model_name='market',
            name='sources',
        ),
        migrations.RemoveField(
            model_name='market',
            name='strategy_recent_investments',
        ),
        migrations.RemoveField(
            model_name='market',
            name='subscription_fee',
        ),
        migrations.RemoveField(
            model_name='market',
            name='turnover_conversion_date',
        ),
        migrations.RemoveField(
            model_name='market',
            name='turnover_currency_rate',
        ),
        migrations.RemoveField(
            model_name='market',
            name='volume_turnover',
        ),
        migrations.RemoveField(
            model_name='market',
            name='volume_turnover_date',
        ),
        migrations.RemoveField(
            model_name='market',
            name='volume_turnover_gbp',
        ),
        migrations.RemoveField(
            model_name='market',
            name='website',
        ),
        migrations.AddField(
            model_name='market',
            name='buyers_customer_service',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='competitor_comparison',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='contact_details',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='customization',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='fee_pricing_structure',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='feedback_system',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='listing_languages',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='logistics_structure',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='market',
            name='merchandising_offer_cost',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='payment_methods',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='payment_terms',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='product_categories',
            field=models.CommaSeparatedIntegerField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='product_category_demand',
            field=models.CommaSeparatedIntegerField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='product_category_size',
            field=models.CommaSeparatedIntegerField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='product_visibility',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='region',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='seller_support_structure',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='shop_analytics',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='size',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='translation_services',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='ukti_terms',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='web_address',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='web_traffic_to_bounce',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='web_traffic_to_site',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
