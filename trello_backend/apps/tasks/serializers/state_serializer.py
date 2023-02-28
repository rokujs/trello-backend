from rest_framework import serializers
from apps.tasks.models.state import State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        exclude = ('date_created', 'date_updated')

    def to_representation(self, instance):
        return {
            'Id': instance.id,
            'Nombre': instance.name,
        }