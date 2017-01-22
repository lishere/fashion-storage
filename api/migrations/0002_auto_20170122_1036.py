# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='invoice_address',
            field=models.ForeignKey(default=1, blank=True, to='api.Invoice_address', null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='shipping_address',
            field=models.ForeignKey(default=1, blank=True, to='api.Shipping_address', null=True),
        ),
    ]
