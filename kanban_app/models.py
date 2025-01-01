from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('urgent', 'Urgent'),
        ('medium', 'Medium'),
        ('low', 'Low')
    ]

    CATEGORY_CHOICES = [
        ('technical', 'Technical'),
        ('userStory', 'User Story')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, default='', blank=True)
    assignedContacts = models.JSONField(default=list)
    dueDate = models.DateField(null=True, blank=True)
    priority = models.CharField(
        max_length=7, choices=PRIORITY_CHOICES)
    category = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES, blank=True, default='')
    subtasks = models.JSONField(default=list)

    def __str__(self):
        return self.title


class Subtask(models.Model):
    task = models.ForeignKey('Task', related_name='subtask', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title