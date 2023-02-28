from rest_framework import generics
from apps.tasks.serializers.state_serializer import StateSerializer


class StateListApiView(generics.ListAPIView):
    serializer_class = StateSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class StateCreateApiView(generics.UpdateAPIView, generics.CreateAPIView):
    serializer_class = StateSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class StateDestroyApiView(generics.RetrieveDestroyAPIView):
    serializer_class = StateSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()