# Generated by Django 4.0.7 on 2022-10-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att_sys', '0003_alter_attendance_chin_alter_attendance_chout_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='remarks',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
    ]
