# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affinity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('VM1', models.CharField(max_length=128)),
                ('VM2', models.CharField(max_length=128)),
                ('VMsOnSameHost', models.CharField(max_length=128)),
                ('VMsInSameCluster', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=128)),
                ('Type', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Backup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('VMName', models.CharField(max_length=128)),
                ('LastBackedup', models.CharField(max_length=128)),
                ('HoursSinceLastBackup', models.CharField(max_length=128)),
                ('MediaServer', models.CharField(max_length=128)),
                ('NBPolicy', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BYOL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('VM', models.CharField(max_length=128)),
                ('cluster', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Capacity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cluster', models.CharField(max_length=128)),
                ('host', models.CharField(max_length=128)),
                ('VM_count', models.CharField(max_length=128)),
                ('CPU_total', models.CharField(max_length=128)),
                ('CPU_allocated', models.CharField(max_length=128)),
                ('RAM_total', models.CharField(max_length=128)),
                ('RAM_allocated', models.CharField(max_length=128)),
                ('CPU_available', models.CharField(max_length=128)),
                ('RAM_available', models.CharField(max_length=128)),
                ('CPU_reserve', models.CharField(max_length=128)),
                ('RAM_reserve', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activeVM_count', models.IntegerField(default=0)),
                ('migrate_count', models.IntegerField(default=0)),
                ('inactive_count', models.IntegerField(default=0)),
                ('cluster_count', models.IntegerField(default=0)),
                ('dcluster_count', models.IntegerField(default=0)),
                ('datastore_count', models.IntegerField(default=0)),
                ('host_count', models.IntegerField(default=0)),
                ('template_count', models.IntegerField(default=0)),
                ('VM_count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SDRS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('VM', models.CharField(max_length=128)),
                ('Enabled', models.CharField(max_length=128)),
                ('cluster', models.CharField(max_length=128)),
                ('report_date', models.ForeignKey(to='dailyhealth.Report')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wrong',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=128)),
                ('Host', models.CharField(max_length=128)),
                ('report_date', models.ForeignKey(to='dailyhealth.Report')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='general',
            name='report_date',
            field=models.ForeignKey(to='dailyhealth.Report'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='capacity',
            name='report_date',
            field=models.ForeignKey(to='dailyhealth.Report'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='byol',
            name='report_date',
            field=models.ForeignKey(to='dailyhealth.Report'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='backup',
            name='report_date',
            field=models.ForeignKey(to='dailyhealth.Report'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alarm',
            name='report_date',
            field=models.ForeignKey(to='dailyhealth.Report'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='affinity',
            name='report_date',
            field=models.ForeignKey(to='dailyhealth.Report'),
            preserve_default=True,
        ),
    ]
