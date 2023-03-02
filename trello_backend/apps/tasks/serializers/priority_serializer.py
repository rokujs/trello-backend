from rest_framework import serializers
from apps.tasks.models.priority import Priority


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'Id': instance.id,
            'Nombre': instance.name,
        }
