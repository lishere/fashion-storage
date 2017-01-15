# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 11:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_product_move_move_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_move',
            name='move_to',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='moveto', to='api.Store'),
        ),
    ]
