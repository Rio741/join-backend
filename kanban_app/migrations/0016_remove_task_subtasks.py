# Generated by Django 5.1.4 on 2025-01-01 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_app', '0015_alter_task_duedate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='subtasks',
        ),
    ]