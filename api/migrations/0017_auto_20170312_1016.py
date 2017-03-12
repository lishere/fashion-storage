# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20170219_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='other_item_amounts',
            field=models.IntegerField(default=0, help_text=b'Add other items amount', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='other_items',
            field=models.TextField(help_text=b'You can add items not included in a sale. Add description for other items here', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='other_items_vat',
            field=models.IntegerField(default=19, help_text=b'VAT to apply on other items in %', null=True, verbose_name=b'Other items VAT', blank=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='sale_vat',
            field=models.IntegerField(default=19, help_text=b'VAT to apply on all items in sale in %', null=True, verbose_name=b'Sale VAT', blank=True),
        ),
    ]
