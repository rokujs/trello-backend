from rest_framework import serializers
from apps.tasks.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            "pk",
            "comment",
            "task"
        )
        read_only_fields = (
            "pk",
        )
