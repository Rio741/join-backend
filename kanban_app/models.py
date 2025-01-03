from django.db import models
from django.conf import settings


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

    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('inProgress', 'In Progress'),
        ('awaitFeedback', 'Awaiting Feedback'),
        ('done', 'Done')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, default='', blank=True)
    assignedContacts = models.JSONField(default=list)
    dueDate = models.DateField(null=True, blank=True)
    priority = models.CharField(
        max_length=7, choices=PRIORITY_CHOICES)
    category = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES, blank=True, default='')
    status = models.CharField(
        max_length=13, choices=STATUS_CHOICES, default='todo')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    ) 

    def __str__(self):
        return self.title


# Subtask Model
class Subtask(models.Model):
    task = models.ForeignKey('Task', related_name='subtasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='in-progress')

    def __str__(self):
        return self.title