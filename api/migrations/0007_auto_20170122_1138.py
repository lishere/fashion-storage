# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20170122_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='resubmission_date',
            field=models.DateField(default=datetime.datetime.now, help_text=b'Mark this data set for resubmission on a date', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='store',
            name='resubmission_date',
            field=models.DateField(default=datetime.datetime.now, help_text=b'Mark this data set for resubmission on a date', null=True, blank=True),
        ),
    ]
