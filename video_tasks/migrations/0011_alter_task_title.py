# Generated by Django 4.1.7 on 2023-02-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_tasks', '0010_alter_task_time_zone_alter_task_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default='task-20230222203758', max_length=200),
        ),
    ]
