from rest_framework import serializers
from apps.tasks.models.state import State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('name', 'id')
        read_only_fields = ("id",)
