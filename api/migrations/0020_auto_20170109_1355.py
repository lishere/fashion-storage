# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20170109_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.AddField(
            model_name='image',
            name='color_1_en',
            field=models.CharField(default='Black', max_length=50, verbose_name=b'Main color in English'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='color_2_en',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'Second color in English'),
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Product'),
        ),
        migrations.AddField(
            model_name='image',
            name='year',
            field=models.SmallIntegerField(blank=True, default=2016, help_text=b'When was this photo taken?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product_variant',
            name='color_1_en',
            field=models.CharField(max_length=50, verbose_name=b'Main color in English'),
        ),
        migrations.AlterField(
            model_name='product_variant',
            name='color_2_en',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'2nd color in English'),
        ),
        migrations.AlterField(
            model_name='product_variant',
            name='color_3_en',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'3rd color in English'),
        ),
        migrations.AlterField(
            model_name='product_variant',
            name='color_4_en',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'4th color in English'),
        ),
        migrations.AlterField(
            model_name='product_variant',
            name='fabric_1_en',
            field=models.CharField(max_length=50, verbose_name=b'Main fabric in English'),
        ),
        migrations.AlterField(
            model_name='product_variant',
            name='fabric_2_en',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'2nd fabric in English'),
        ),
        migrations.AlterField(
            model_name='product_variant',
            name='fabric_3_en',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'3nd fabric in English'),
        ),
        migrations.AlterField(
            model_name='product_variant',
            name='fabric_4_en',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'4nd fabric in English'),
        ),
    ]