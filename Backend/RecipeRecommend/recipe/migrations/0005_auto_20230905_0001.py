# Generated by Django 3.2.20 on 2023-09-04 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20230904_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='dietary_preferences',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='shoping_list',
            field=models.JSONField(default=list),
        ),
    ]