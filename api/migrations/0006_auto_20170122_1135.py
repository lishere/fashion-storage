# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_customer_resubmission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='resubmission_date',
            field=models.DateField(default=datetime.datetime.now, help_text=b'Mark this data set for resubmission on a date', null=True, blank=True),
        ),
    ]
