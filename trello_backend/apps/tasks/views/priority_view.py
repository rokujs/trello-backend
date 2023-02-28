from rest_framework import generics
from apps.tasks.serializers.priority_serializer import PrioritySerializer


class PriorityListApiView(generics.ListAPIView):
    serializer_class = PrioritySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class PriorityCreateApiView(generics.UpdateAPIView, generics.CreateAPIView):
    serializer_class = PrioritySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class PriorityDestroyApiView(generics.RetrieveDestroyAPIView):
    serializer_class = PrioritySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()