# Generated by Django 3.1.1 on 2021-11-20 00:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('votingapp', '0005_auto_20211119_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='votes',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='poll',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 0, 44, 21, 687348, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='poll',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 0, 44, 21, 687385, tzinfo=utc)),
        ),
    ]
