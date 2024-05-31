from rest_framework import serializers
from .models import WalletModel
from user.models import User
from user.serializers import UserSerializerShow

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletModel
        fields = ["id","balance", "user"]
        depth = 1

class WalletCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = WalletModel
        fields = ["user"]

class WalletUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletModel
        fields = ["balance"]