# Generated by Django 4.2.8 on 2024-01-03 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_habits', '0006_alter_habit_start_date_alter_habit_time_to_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='start_date',
        ),
    ]
