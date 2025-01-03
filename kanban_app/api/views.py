from rest_framework import viewsets
from kanban_app.models import Task, Subtask
from .serializers import TaskSerializer, SubtaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Task ViewSet
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        task = self.get_object()
        print("Request Data:", request.data)  # Log-Ausgabe für Debugging
        status = request.data.get('status', task.status)
        task.status = status
        task.save()
        return Response({'status': task.status})


class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        subtask = self.get_object()
        new_status = request.data.get('status')
        if new_status:
            subtask.status = new_status
            subtask.save()
            return Response({'id': subtask.id, 'status': subtask.status}, status=200)
        return Response({'error': 'Status not provided'}, status=400)
