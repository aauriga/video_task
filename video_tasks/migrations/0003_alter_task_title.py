# Generated by Django 4.1.7 on 2023-02-20 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_tasks', '0002_task_end_time_task_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default='task-20230220210926', max_length=200),
        ),
    ]
