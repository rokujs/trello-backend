from rest_framework import serializers
from apps.tasks.models.task import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            "pk",
            "name",
            "description",
            "state",
            "priority",
            "dateline"
        )
        read_only_fields = (
            "pk",
        )


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


    def to_representation(self, instance):
        return {
            'Id': instance.id,
            'Nombre': instance.name,
            'Descripción': instance.description,
            'Estado': instance.state.__str__(),
            'Prioridad': instance.priority.__str__(),
            'Fecha de finalizacion': instance.dateline
        }
