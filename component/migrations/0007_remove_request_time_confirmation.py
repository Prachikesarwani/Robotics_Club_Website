# Generated by Django 3.0.3 on 2021-02-06 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0006_auto_20210206_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='time_confirmation',
        ),
    ]
