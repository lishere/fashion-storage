# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20170110_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_variant',
            name='rec_gross_sale_price_by_country',
            field=models.ManyToManyField(blank=True, to='api.Product_variant_price_per_country'),
        ),
    ]
