# Generated by Django 5.0.4 on 2024-04-19 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_rename_plantype_trainingfocus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='plan_type',
            new_name='training_focus',
        ),
    ]
