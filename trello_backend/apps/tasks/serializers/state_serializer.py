from rest_framework import serializers
from apps.tasks.models.state import State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'Id': instance.id,
            'Nombre': instance.name,
        }
