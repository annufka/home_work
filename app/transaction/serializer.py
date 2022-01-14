from django.contrib.auth.models import User
from rest_framework import serializers

from app.transaction.models import Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Transaction
        fields = "__all__"
