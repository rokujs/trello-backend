from rest_framework import serializers

from apps.tasks.models import Comment
from apps.security.serializers.user_serializer import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "pk",
            "comment",
            "task",
            "user"
        )
        read_only_fields = (
            "pk",
        )


class CommentTaskSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'comment')
