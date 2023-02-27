from rest_framework import serializers
from apps.tasks.models import Comment


class commentSerializer(serializers.ModelSerializer):

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
