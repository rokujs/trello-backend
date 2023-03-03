from rest_framework import serializers

from apps.tasks.models import Task, Comment
from apps.security.serializers.user_serializer import UserSerializer
from apps.tasks.serializers.comment_serializer import CommentTaskSerializer


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ("id", "name", "description",
                  "state_id", "priority_id", "dateline", "users")
        read_only_fields = ("id",)

    def to_representation(self, instance):
        comments = Comment.objects.filter(task=instance)
        comments = CommentTaskSerializer(comments, many=True).data

        users = UserSerializer(instance.users, many=True).data
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'state': instance.state.__str__(),
            'priority': instance.priority.__str__(),
            'dateline': instance.dateline,
            'comments': comments,
            "assigned_users": users
        }
