# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20170312_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='currency',
            field=models.CharField(default=b'EUR', max_length=3, blank=True, choices=[(b'other', b'Other currency'), (b'EUR', b'Euro'), (b'GBP', b'British Pound'), (b'CAD', b'Canadian Dollar'), (b'DKK', b'Danish Krone'), (b'NOK', b'Norwegian Krone'), (b'RUB', b'Russian Rubel'), (b'SEK', b'Swedish Krona'), (b'CHF', b'Swiss Franken'), (b'USD', b'US Dollar')]),
        ),
        migrations.AddField(
            model_name='invoice',
            name='general_description',
            field=models.TextField(help_text=b'Other text to add to this invoice', null=True, verbose_name=b'Other text', blank=True),
        ),
    ]
