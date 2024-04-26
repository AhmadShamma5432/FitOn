# Generated by Django 5.0.4 on 2024-04-18 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_exerciseday_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='day',
        ),
        migrations.RemoveField(
            model_name='exerciseday',
            name='day',
        ),
        migrations.RemoveField(
            model_name='exerciseday',
            name='exercise',
        ),
        migrations.AlterUniqueTogether(
            name='exerciseday',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='exerciseday',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='plan_type',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.DeleteModel(
            name='ExerciseDay',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
