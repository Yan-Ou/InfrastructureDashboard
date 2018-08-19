# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailyhealth', '0002_snapshot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zombie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=128)),
                ('Message', models.CharField(max_length=128)),
                ('report_date', models.ForeignKey(to='dailyhealth.Report')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
