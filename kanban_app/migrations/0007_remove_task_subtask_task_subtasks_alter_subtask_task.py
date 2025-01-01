# Generated by Django 5.1.4 on 2024-12-31 00:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_app', '0006_subtask'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='subtask',
        ),
        migrations.AddField(
            model_name='task',
            name='subtasks',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtask', to='kanban_app.task'),
        ),
    ]