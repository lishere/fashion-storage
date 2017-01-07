# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 07:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_store_contact_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('items_bought', models.IntegerField(blank=True, default=0)),
                ('wants_newsletter', models.BooleanField(default=True)),
                ('language', models.CharField(choices=[(b'DE', b'German'), (b'EN', b'English')], default=b'DE', max_length=2)),
                ('gender', models.CharField(choices=[(b'F', b'Female'), (b'M', b'Male')], default=b'F', max_length=1)),
                ('given_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=125)),
                ('zip_code', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('facebook', models.URLField(blank=True, max_length=250)),
                ('twitter', models.URLField(blank=True, max_length=250)),
                ('instagram', models.URLField(blank=True, max_length=250)),
                ('pinterest', models.URLField(blank=True, max_length=250)),
                ('country', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.Country')),
            ],
            options={
                'ordering': ('given_name', 'surname'),
            },
        ),
    ]