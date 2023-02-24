from rest_framework import serializers
from apps.tasks.models.task import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

    # def create(self):
    #     pass
    #
    # def update(self):
    #     pass

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
    
    def get_txt(column, index):
        if column == 'state':
            txt = [x[1] for x in Task.STATE if x[0] == index]
            if txt:
                return txt[0]
            else:
                return "" 
            
        if column == 'priority':
            txt = [x[1] for x in Task.STATE if x[0] == index]
            if txt:
                return txt[0]
            else:
                return "" 
    
    def to_representation(self, instance):
        return {
            'Id': instance['id'],
            'Nombre': instance['name'],
            'Descripción': instance['description'],
            'Estado': get_txt('state', instance['state']),
            'Prioridad': get_txt('priority', instance['priority']),
            'Fecha de finalizacion': instance['dateline']
        }