# Generated by Django 4.2.3 on 2023-08-02 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50, verbose_name='место')),
                ('time', models.TimeField(verbose_name='время')),
                ('action', models.CharField(max_length=150, verbose_name='действие')),
                ('pleasurable_habit', models.CharField(max_length=50, verbose_name='признак приятной привычки')),
                ('linked_habit', models.CharField(max_length=50, verbose_name='cвязанная привычка')),
                ('frequency', models.DateField(default=datetime.date.today, verbose_name='периодичность')),
                ('reward', models.CharField(max_length=150, verbose_name='вознаграждение')),
                ('time_to_complete', models.DateTimeField(verbose_name='время на выполнение ')),
                ('sign_of_publicity', models.CharField(max_length=150, verbose_name='признак публичности')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
