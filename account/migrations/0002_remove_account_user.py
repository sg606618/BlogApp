# Generated by Django 5.0.6 on 2024-07-07 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
    ]
