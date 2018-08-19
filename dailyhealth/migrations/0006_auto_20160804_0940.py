# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailyhealth', '0005_auto_20160804_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='removed',
            name='Message',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
