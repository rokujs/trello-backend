from rest_framework import generics
from apps.tasks.serializers.priority_serializer import PrioritySerializer


class PriorityListApiView(generics.ListCreateAPIView):
    serializer_class = PrioritySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class PriorityUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PrioritySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
