# Generated by Django 4.1.4 on 2023-01-05 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication_and_User_Management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='theme_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='theme_value',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]