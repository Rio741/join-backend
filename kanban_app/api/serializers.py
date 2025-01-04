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
        subtasks_data = validated_data.pop('subtasks', None)
        
        # Update der Task-Attribute
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
    
        # Subtasks verarbeiten
        if subtasks_data is not None:
            existing_subtasks = list(instance.subtasks.all())
            existing_ids = {subtask.id for subtask in existing_subtasks}
    
            # Aktualisieren oder Hinzufügen von Subtasks
            for subtask_data in subtasks_data:
                subtask_id = subtask_data.get('id')
                if subtask_id in existing_ids:
                    subtask = next(sub for sub in existing_subtasks if sub.id == subtask_id)
                    for attr, value in subtask_data.items():
                        setattr(subtask, attr, value)
                    subtask.save()
                else:
                    Subtask.objects.create(task=instance, **subtask_data)
    
            # Entfernen von Subtasks, die nicht mehr in den neuen Daten enthalten sind
            new_ids = {subtask.get('id') for subtask in subtasks_data if subtask.get('id')}
            for subtask in existing_subtasks:
                if subtask.id not in new_ids:
                    subtask.delete()
    
        return instance

