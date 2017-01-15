# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20170110_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_variant_price_per_country',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Country'),
        ),
        migrations.AlterField(
            model_name='product_variant_price_per_country',
            name='rec_gross_sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name=b'Recommended gross sale price in the currency of the country'),
        ),
    ]