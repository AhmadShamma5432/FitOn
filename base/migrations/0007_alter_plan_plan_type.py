# Generated by Django 5.0.4 on 2024-04-10 08:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_plan_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='plan_type',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.plantype'),
        ),
    ]
