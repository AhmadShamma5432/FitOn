# Generated by Django 5.0.4 on 2024-04-16 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_trainee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='plan_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.plantype'),
        ),
    ]
