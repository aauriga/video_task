# Generated by Django 4.1.7 on 2023-02-24 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_tasks', '0015_alter_task_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default='task-20230224162009', max_length=200),
        ),
    ]
