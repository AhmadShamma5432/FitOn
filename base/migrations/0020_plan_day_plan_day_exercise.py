# Generated by Django 5.0.4 on 2024-04-18 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_day_exercise_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan_Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day_rel', to='base.day')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_rel', to='base.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Plan_Day_Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.PositiveSmallIntegerField()),
                ('reps', models.PositiveSmallIntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_rel', to='base.exercise')),
                ('plan_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_day_rel', to='base.plan_day')),
            ],
        ),
    ]
