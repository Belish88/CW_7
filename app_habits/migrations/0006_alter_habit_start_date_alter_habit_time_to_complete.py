# Generated by Django 4.2.8 on 2024-01-03 16:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_habits', '0005_habit_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date(2024, 1, 3), null=True, verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time_to_complete',
            field=models.PositiveIntegerField(default=60, verbose_name='Время на выполнение'),
        ),
    ]
