# Generated by Django 5.0.4 on 2024-04-21 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_mainadvice_subadvice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingfocus',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]
