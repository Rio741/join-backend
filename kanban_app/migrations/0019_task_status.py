# Generated by Django 5.1.4 on 2025-01-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban_app', '0018_subtask_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('urgent', 'Urgent'), ('medium', 'Medium'), ('low', 'Low')], default='', max_length=13),
        ),
    ]
