# Generated by Django 4.1.7 on 2023-02-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_tasks', '0007_task_creator_alter_task_title_alter_task_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='task',
            name='upload_time',
            field=models.CharField(choices=[('now', 'now'), ('regular', 'regular')], default='regular', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default='task-20230222175121', max_length=200),
        ),
    ]
