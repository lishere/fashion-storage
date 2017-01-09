# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20170107_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_variant',
            name='color_1',
        ),
        migrations.RemoveField(
            model_name='product_variant',
            name='color_2',
        ),
        migrations.RemoveField(
            model_name='product_variant',
            name='color_3',
        ),
        migrations.RemoveField(
            model_name='product_variant',
            name='color_4',
        ),
        migrations.RemoveField(
            model_name='product_variant',
            name='fabric_1',
        ),
        migrations.RemoveField(
            model_name='product_variant',
            name='fabric_2',
        ),
        migrations.RemoveField(
            model_name='product_variant',
            name='fabric_3',
        ),
        migrations.RemoveField(
            model_name='product_variant',
            name='fabric_4',
        ),
        migrations.AddField(
            model_name='product_variant',
            name='color_1_de',
            field=models.CharField(default='Schwarz', max_length=50, verbose_name=b'Main color in German'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_variant',
            name='color_1_en',
            field=models.CharField(default='Black', max_length=50, verbose_name=b'Main color in Englisch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_variant',
            name='color_1_it',
            field=models.CharField(default='Nero', max_length=50, verbose_name=b'Main color in Italian'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_variant',
            name='color_2_de',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'2nd color in German'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='color_2_en',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'2nd color in Englisch'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='color_2_it',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'2nd color in Italian'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='color_3_de',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'3rd color in German'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='color_3_en',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'3rd color in Englisch'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='color_3_it',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'3rd color in Italian'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='color_4_de',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'4th color in German'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='color_4_en',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'4th color in Englisch'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='color_4_it',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'4th color in Italian'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='fabric_1_de',
            field=models.CharField(default='Baumwolle', max_length=50, verbose_name=b'Main fabric in German'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_variant',
            name='fabric_1_en',
            field=models.CharField(default='Cotton', max_length=50, verbose_name=b'Main fabric in Enlish'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_variant',
            name='fabric_1_it',
            field=models.CharField(default='Cotone', max_length=50, verbose_name=b'Main fabric in Italian'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_variant',
            name='fabric_2_de',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'2nd fabric in German'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='fabric_2_en',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'2nd fabric in Englisch'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='fabric_2_it',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'2nd fabric in Italian'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='fabric_3_de',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'3nd fabric in German'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='fabric_3_en',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'3nd fabric in Englisch'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='fabric_3_it',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'3nd fabric in Italian'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='fabric_4_de',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'4nd fabric in German'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='fabric_4_en',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'4nd fabric in Englisch'),
        ),
        migrations.AddField(
            model_name='product_variant',
            name='fabric_4_it',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'4nd fabric in Italian'),
        ),
    ]
