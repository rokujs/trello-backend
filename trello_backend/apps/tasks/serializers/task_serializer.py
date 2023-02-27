from rest_framework import serializers

from apps.tasks.models import Task, Comment


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
        comments = Comment.objects.filter(
            task=instance).values_list("comment", flat=True)
        return {
            'Id': instance.id,
            'Nombre': instance.name,
            'Descripción': instance.description,
            'Estado': None if instance.state == None else [x for x in Task.STATE if x[0] == instance.state][0][1],
            'Prioridad': None if instance.priority == None else [x for x in Task.PRIORITY if x[0] == instance.priority][0][1],
            'Fecha de finalizacion': instance.dateline,
            'Comentaríos': comments
        }
