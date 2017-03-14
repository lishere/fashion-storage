# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20170312_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='other_item_amounts',
            new_name='other_items_amount',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='correction_for',
            field=models.ForeignKey(related_name='selfref', blank=True, to='api.Invoice', help_text=b'Choose here if this invoice is a correction for a previous invoice', null=True),
        ),
    ]
