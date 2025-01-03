from rest_framework import serializers
from kanban_app.models import Task, Subtask


# Subtask Serializer
class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'title', 'status']


# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assignedContacts', 'dueDate', 'priority', 'category', 'subtasks', 'status']

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        task = Task.objects.create(**validated_data)

        # Erstelle Subtasks, wenn sie vorhanden sind
        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)

        return task

    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        
        # Update der Task-Attribute
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Subtasks aktualisieren
        if subtasks_data is not None:  # Nur aktualisieren, wenn es Subtasks gibt
            # Lösche alte Subtasks und erstelle neue, falls nötig
            if subtasks_data:
                instance.subtasks.all().delete()  # Alte Subtasks löschen
                Subtask.objects.bulk_create(
                    [Subtask(task=instance, **subtask_data) for subtask_data in subtasks_data]
                )
            else:
                # Wenn keine Subtasks übergeben werden, lösche die alten
                instance.subtasks.all().delete()

        return instance
