# Generated by Django 4.0.7 on 2022-10-18 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att_sys', '0008_alter_attendance_chout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='chin',
            field=models.TimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='chout',
            field=models.TimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]