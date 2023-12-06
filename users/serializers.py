from django.utils.crypto import get_random_string
from rest_framework import serializers
from django.contrib.auth.models import User


class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=255)


class UserLoginSerializer(UserValidateSerializer):
    pass


class UserRegisterSerializer(UserValidateSerializer):

    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(max_length=50, required=False)
    last_name = serializers.CharField(max_length=50, required=False)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.is_active = False
        confirmation_code = get_random_string(length=6)
        user.confirmation_code = confirmation_code
        user.save()

        return user


class UserProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'is_staff', 'is_superuser', 'is_active', 'date_joined',
                  'last_login']