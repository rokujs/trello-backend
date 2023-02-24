from rest_framework import generics

from apps.tasks.models import Task
from apps.tasks.serializers import TaskSerializer, TaskListSerializer
from apps.tasks.filters import TaskFilter


class TaskApiView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    filterset_fields = ('pk', 'name', 'id')
    filterset_class = TaskFilter


class TaskCreateUpdateApiView(generics.UpdateAPIView, generics.CreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
