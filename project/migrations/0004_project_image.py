# Generated by Django 3.0.3 on 2021-02-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='default-project.png', upload_to='projects'),
        ),
    ]
