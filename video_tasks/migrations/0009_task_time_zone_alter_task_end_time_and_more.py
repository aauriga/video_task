# Generated by Django 4.1.7 on 2023-02-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_tasks', '0008_remove_task_due_date_remove_task_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time_zone',
            field=models.CharField(choices=[('UTC', 'utc'), ('CST', 'cst'), ('MST', 'mst'), ('PST', 'pst'), ('AST', 'ast'), ('EST', 'est'), ('HST', 'hst'), ('AKST', 'akst')], default='cst', max_length=5),
        ),
        migrations.AlterField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default='task-20230222181324', max_length=200),
        ),
    ]
