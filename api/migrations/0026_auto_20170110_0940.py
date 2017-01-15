# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20170110_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_variant',
            name='rec_gross_sale_price_default',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, verbose_name=b'Recommended default gross sale price in EURO'),
        ),
    ]