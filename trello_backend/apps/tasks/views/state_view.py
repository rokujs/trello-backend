from rest_framework import generics
from apps.tasks.serializers.state_serializer import StateSerializer


class StateListCreateApiView(generics.ListCreateAPIView):
    serializer_class = StateSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class StateUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StateSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
