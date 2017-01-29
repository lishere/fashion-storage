# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-29 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20170129_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_move',
            name='move_type',
        ),
        migrations.AddField(
            model_name='product_move',
            name='is_destroyed',
            field=models.BooleanField(default=False, help_text=b'Mark this item as destroyed, stolen or otherwise non-saleable', verbose_name=b'Destroyed?'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sold_to_store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='soldtostore', to='api.Store', verbose_name=b'Sold in store / Sold to store'),
        ),
    ]
