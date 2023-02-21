# Generated by Django 4.1.7 on 2023-02-21 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0009_remove_agency_something'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='city',
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='travel.country'),
        ),
    ]
