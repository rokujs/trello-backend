from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics
from apps.tasks.models.task import Task
from apps.tasks.api.serializers.serializers import TaskSerializer, TaskListSerializer


class TaskListApiView(generics.ListAPIView):
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

class TaskCreateApiView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    
class TaskRetriviewApiView(generics.RetrieveAPIView):
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
class TaskDestroyApiView(generics.DestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
class TaskUpdateApiView(generics.UpdateAPIView):
    serializer_class = TaskSerializer

""" @api_view(['GET', 'POST'])
def task_api_view(request):
#     list
    if request.method == 'GET':
#         queryset
        tasks = Task.objects.all().values('id','name','description','state','priority','dateline')
        tasks_serializer = TaskListSerializer(tasks, many=True)
        return Response(tasks_serializer.data, status=status.HTTP_200_OK)
#     create
    elif request.method == 'POST':
        task_serializer = TaskSerializer(data = request.data)

        #         validation
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data, status=status.HTTP_201_CREATED)
        return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail_api_view(request, pk=None):
#     queryset
    task = Task.objects.filter(id = pk).first()
    print(task)
#     validation
    if task:

#         retrive
        if request.method == 'GET':
            task_serializer = TaskSerializer(task)
            return Response(task_serializer.data, status=status.HTTP_200_OK)

#         update
        elif request.method == 'PUT':
            task_serializer = TaskSerializer(task, data=request.data)
            if task_serializer.is_valid():
                task_serializer.save()
                return Response(task_serializer.data, status=status.HTTP_200_OK)
            return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         delete
        elif request.method == 'DELETE':
            task.delete()
            return Response({'message': 'Tarea eliminada correctamente!'}, status=status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado una tarea con estos datos'}, status=status.HTTP_400_BAD_REQUEST) """