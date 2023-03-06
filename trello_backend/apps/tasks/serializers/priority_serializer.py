from rest_framework import serializers
from apps.tasks.models.priority import Priority


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ('id', 'name')
        read_only_fields = ("id",)
