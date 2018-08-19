# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailyhealth', '0004_cdrom_clone_removed_reservation_storageio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='removed',
            name='Message',
            field=models.CharField(max_length=256),
            preserve_default=True,
        ),
    ]
