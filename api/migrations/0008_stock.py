# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170122_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=0, blank=True)),
                ('product_variant', models.ForeignKey(to='api.Product_variant')),
                ('store', models.ForeignKey(to='api.Store')),
            ],
            options={
                'ordering': ('created',),
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
            },
        ),
    ]
