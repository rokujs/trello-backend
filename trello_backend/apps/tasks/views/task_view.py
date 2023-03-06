from rest_framework import generics

from apps.tasks.models import Task
from apps.tasks.serializers.task_serializer import TaskSerializer
from apps.tasks.filters import TaskFilter


class TaskApiView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = ('pk', 'name', 'id')
    filterset_class = TaskFilter


class TaskUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
