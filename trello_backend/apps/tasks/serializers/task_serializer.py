from rest_framework import serializers

from apps.tasks.models import Task, Comment
from apps.security.serializers.user_serializer import UserSerializer
from apps.tasks.serializers.comment_serializer import CommentTaskSerializer


def representation(instance):
    comments = Comment.objects.filter(task=instance)
    comments = CommentTaskSerializer(comments, many=True).data

    users = UserSerializer(instance.users, many=True).data
    return {
        'Id': instance.id,
        'Nombre': instance.name,
        'Descripción': instance.description,
        'Estado': instance.state.__str__(),
        'Prioridad': instance.priority.__str__(),
        'Fecha de finalizacion': instance.dateline,
        'Comentarios': comments,
        "Usuarios asignados": users
    }


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ("pk", "name", "description",
                  "state_id", "priority_id", "dateline", "users")
        read_only_fields = ("pk",)

    def to_representation(self, instance):
        return representation(instance)


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        return representation(instance)
