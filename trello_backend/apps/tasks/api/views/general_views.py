from rest_framework import generics

from apps.tasks.api.serializers.general_serializers import PrioritySerializer, StateSerializer
# from apps.tasks.models.priority import Priority
# from apps.tasks.models.state import State

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

##############################################################

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