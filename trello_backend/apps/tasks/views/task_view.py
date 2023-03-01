from rest_framework import generics

from apps.tasks.models import Task
from apps.tasks.serializers.task_serializer import TaskSerializer, TaskListSerializer
from apps.tasks.filters import TaskFilter


class TaskApiView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    filterset_fields = ('pk', 'name', 'id')
    filterset_class = TaskFilter

<<<<<<< HEAD
class TaskCreateUpdateApiView(generics.UpdateAPIView, generics.CreateAPIView):
=======

class TaskCreateApiView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskUpdateApiView(generics.UpdateAPIView):
>>>>>>> develop
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TaskDestroyApiView(generics.RetrieveDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()