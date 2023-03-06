from rest_framework import serializers

from apps.security.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "bio",
                  "first_name", "last_name", "password")
        read_only_fields = ("id",)

    def create(self, validated_data):
        request = self.context.get("request")
        password = request.data.get("password")

        user = User.objects.create(**validated_data)
        user.set_password(password)

        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.bio = validated_data.get("bio", instance.bio)
        instance.first_name = validated_data.get(
            "first_name", instance.first_name)
        instance.last_name = validated_data.get(
            "last_name", instance.last_name)

        password = validated_data.get("password")

        if password:
            instance.set_password(password)

        instance.save()

        return instance

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'email': instance.email,
            'names': instance.get_full_name(),
            'bio': instance.bio,
        }
