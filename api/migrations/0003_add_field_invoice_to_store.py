# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170106_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='invoice_address',
            field=models.ForeignKey(blank=True, default=1, to='api.Invoice_address'),
        ),
    ]