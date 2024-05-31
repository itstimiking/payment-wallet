from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from .models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token



class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = (
            "user_id",
            "email",
            'password',
            "firstname",
            "lastname",
            "bio",
            "sex",
            "avatar",
            "banner",
        )

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = (
            "user_id",
            "email",
            'password',
            "firstname",
            "lastname",
            "bio",
            "sex",
            "avatar",
            "banner",
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            'password',
        )
        
        
class UserSerializerShow(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "user_id",
            "email",
            "firstname",
            "lastname",
            "bio",
            "sex",
            "avatar",
            "banner",
            "status",
            "created_date",
            "updated_date",
        ]
        
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "user_id",
            "email",
            "firstname",
            "lastname",
            "bio",
            "sex",
            "avatar",
            "banner",
            "status",
        ]