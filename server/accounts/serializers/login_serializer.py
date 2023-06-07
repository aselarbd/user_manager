from django.contrib.auth import authenticate
from rest_framework import serializers
from server.accounts.models import CustomUser


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email').lower()
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError('Please provide both email and password.')

        if not CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('Provided email does not exist.')

        user = authenticate(request=self.context.get('request'), email=email, password=password)

        if not user:
            raise serializers.ValidationError('Provided credentials are wrong.')

        attrs['user'] = user
        return attrs
