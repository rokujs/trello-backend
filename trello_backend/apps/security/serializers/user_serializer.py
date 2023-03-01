from rest_framework import serializers

from apps.security.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("pk", "username", "email", "bio",
                  "first_name", "last_name", "password")
        read_only_fields = ("pk",)

    def create(self, validated_data):
        request = self.context.get("request")
        password = request.data.get("password")

        user = User.objects.create(**validated_data)
        user.set_password(password)

        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.get("password")

        if password:
            instance.set_password(password)
            instance.save()

        return instance

    def to_representation(self, instance):
        return {
            'Id': instance.id,
            'Email': instance.email,
            'Nombre': instance.get_full_name(),
            'Biografia': instance.bio,
        }
