# Generated by Django 5.0.4 on 2024-05-11 15:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=6)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('health_conditions', models.TextField(blank=True, null=True)),
                ('fitness_goals', models.TextField(blank=True, null=True)),
                ('sessions_completed', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('progress_notes', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=6)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('specialities', models.CharField(max_length=200)),
                ('experience_years', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('working_hours', models.CharField(max_length=100)),
                ('instagram_profile', models.URLField(blank=True, null=True)),
                ('twitter_profile', models.URLField(blank=True, null=True)),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='client',
            constraint=models.CheckConstraint(check=models.Q(('gender', 'M'), ('gender', 'F'), _connector='OR'), name='Check_Client_Gender'),
        ),
        migrations.AddConstraint(
            model_name='trainer',
            constraint=models.CheckConstraint(check=models.Q(('gender', 'M'), ('gender', 'F'), _connector='OR'), name='Check_Trainee_Gender'),
        ),
    ]
