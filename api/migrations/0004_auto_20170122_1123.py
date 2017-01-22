# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_store_is_agency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='items_bought',
            field=models.IntegerField(default=0, verbose_name=b'Total number of items bought by this customer', blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='commission_rate',
            field=models.IntegerField(default=50, help_text=b'Commmission as charged by this partner in %', blank=True),
        ),
    ]
