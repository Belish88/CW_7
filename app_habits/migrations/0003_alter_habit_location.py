# Generated by Django 4.2.8 on 2023-12-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_habits', '0002_alter_habit_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Место'),
        ),
    ]
