from rest_framework import serializers
from apps.tasks.models.task import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        exclude = ('date_created', 'date_updated')


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
    
    def to_representation(self, instance):
        return {
            'Id': instance.id,
            'Nombre': instance.name,
            'Descripción': instance.description,
            'Estado': None if instance.state == None else [x for x in Task.STATE if x[0] == instance.state][0][1],
            'Prioridad': None if instance.priority == None else [x for x in Task.PRIORITY if x[0] == instance.priority][0][1],
            'Fecha de finalizacion': instance.dateline
        }