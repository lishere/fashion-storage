# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20170122_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='resubmission_date',
            field=models.DateField(help_text=b'Mark this data set for resubmission on a date', auto_now=True, null=True),
        ),
    ]
