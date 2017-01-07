# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_address',
            name='contact_person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Person'),
        ),
    ]
