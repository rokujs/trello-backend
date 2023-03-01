from rest_framework import serializers
from apps.tasks.models.priority import Priority


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        exclude = ('date_created', 'date_updated')

    def to_representation(self, instance):
        return {
            'Id': instance.id,
            'Nombre': instance.name,
        }