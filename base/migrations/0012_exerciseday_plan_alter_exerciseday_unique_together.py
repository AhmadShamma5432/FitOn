# Generated by Django 5.0.4 on 2024-04-16 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_plan_plan_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerciseday',
            name='plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.plan'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='exerciseday',
            unique_together={('exercise', 'day', 'plan')},
        ),
    ]
