# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170122_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='is_agency',
            field=models.BooleanField(default=False, help_text=b'Is this partner an agency?'),
        ),
    ]
