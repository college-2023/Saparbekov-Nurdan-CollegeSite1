from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed


class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = 'username email password password2'.split()
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        user.is_active = False
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if User.objects.filter(email=user.email).exists():
            raise serializers.ValidationError({'email': 'Username with this email already exists'})

        if password != password2:
            raise serializers.ValidationError({"password": "Passwords didn't match"})
        user.set_password(password)
        user.save()
        return user


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ("email",)

#
# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(read_only=True)
#     name = serializers.CharField(read_only=True)
#     username = serializers.CharField()
#     tokens = serializers.CharField(read_only=True)
#     password = serializers.CharField(write_only=True, style={"input_type": "password"})
#
#     def validate(self, attrs):
#         username = attrs.get("username", "")
#         password = attrs.get("password", "")
#         user = auth.authenticate(username=username, password=password)
#         if not user:
#             raise AuthenticationFailed("Invalid credentials, try again")
#         if not user.is_active:
#             raise AuthenticationFailed("Email is not verified")
#         return {
#             "email": user.email,
#             "username": user.username,
#         }

