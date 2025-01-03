from rest_framework import viewsets
from kanban_app.models import Task, Subtask
from .serializers import TaskSerializer, SubtaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions import IsStaffOrReadOnly
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # user statt owner

    def get_queryset(self):
        # Nur die Tasks des authentifizierten Benutzers anzeigen
        return Task.objects.filter(user=self.request.user)  # user statt owner



    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        task = self.get_object()
        status = request.data.get('status', task.status)
        if status not in dict(Task.STATUS_CHOICES):
            return Response({'error': 'Invalid status'}, status=400)
        task.status = status
        task.save()
        return Response({'id': task.id, 'status': task.status}, status=200)



class SubtaskViewSet(viewsets.ModelViewSet):
    serializer_class = SubtaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtere Subtasks, die zu den Tasks des authentifizierten Benutzers gehören
        return Subtask.objects.filter(task__user=self.request.user)


    def perform_create(self, serializer):
        # Verknüpfe den Subtask mit einem Task
        serializer.save()

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        subtask = self.get_object()
        new_status = request.data.get('status')
        if new_status not in ['in-progress', 'done']:
            return Response({'error': 'Invalid status'}, status=400)
        subtask.status = new_status
        subtask.save()
        return Response({'id': subtask.id, 'status': subtask.status}, status=200)
