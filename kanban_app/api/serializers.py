from rest_framework import serializers
from kanban_app.models import Task, Subtask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assignedContacts', 'dueDate', 'priority', 'category', 'subtask']


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'task', 'title']