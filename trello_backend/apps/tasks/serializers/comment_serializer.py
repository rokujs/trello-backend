from rest_framework import serializers

from apps.tasks.models import Comment
from apps.security.serializers.user_serializer import UserSerializer


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            "id",
            "comment",
            "task",
            "user"
        )
        read_only_fields = (
            "id", "user"
        )

    def create(self, validated_data):
        user = self.context['request'].user
        comment = Comment.objects.create(user=user, **validated_data)
        return comment


class CommentTaskSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'user', 'comment')
