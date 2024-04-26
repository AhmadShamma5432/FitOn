# Generated by Django 5.0.4 on 2024-04-19 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_rename_plan_type_plan_training_focus'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainAdvice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SubAdvice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('main_advice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_advices', to='base.mainadvice')),
            ],
        ),
    ]
