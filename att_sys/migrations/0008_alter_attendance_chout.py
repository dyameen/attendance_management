# Generated by Django 4.0.7 on 2022-10-17 15:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('att_sys', '0007_alter_attendance_chout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='chout',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]