# Generated by Django 3.2.20 on 2023-08-30 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dietary_preferences',
            field=models.JSONField(blank=True, default=list),
        ),
    ]