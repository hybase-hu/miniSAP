# Generated by Django 4.0.1 on 2022-08-18 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_task_finished_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_seen',
            field=models.BooleanField(default=False),
        ),
    ]
