# Generated by Django 4.2.8 on 2024-01-01 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_habits', '0003_alter_habit_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodic',
            field=models.CharField(blank=True, choices=[('1', '1 День'), ('2', '2 Дня'), ('3', '3 Дня'), ('4', '4 Дня'), ('5', '5 Дней'), ('6', '6 Дней'), ('7', '7 Дней')], default='1', max_length=2, null=True, verbose_name='Периодичность'),
        ),
    ]
