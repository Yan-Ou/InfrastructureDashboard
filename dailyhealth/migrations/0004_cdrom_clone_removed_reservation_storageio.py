# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailyhealth', '0003_zombie'),
    ]

    operations = [
        migrations.CreateModel(
            name='CDROM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('VM', models.CharField(max_length=128)),
                ('report_date', models.ForeignKey(to='dailyhealth.Report')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CreatedTime', models.CharField(max_length=128)),
                ('UserName', models.CharField(max_length=128)),
                ('Message', models.CharField(max_length=128)),
                ('report_date', models.ForeignKey(to='dailyhealth.Report')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Removed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CreatedTime', models.CharField(max_length=128)),
                ('UserName', models.CharField(max_length=128)),
                ('Message', models.CharField(max_length=128)),
                ('report_date', models.ForeignKey(to='dailyhealth.Report')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=128)),
                ('CPURes', models.CharField(max_length=128)),
                ('MemRes', models.CharField(max_length=128)),
                ('report_date', models.ForeignKey(to='dailyhealth.Report')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StorageIO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=128)),
                ('IOControl', models.CharField(max_length=128)),
                ('report_date', models.ForeignKey(to='dailyhealth.Report')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
