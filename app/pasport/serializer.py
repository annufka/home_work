from django.contrib.auth.models import User
from rest_framework import serializers

from app.pasport.models import Pasport

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PasportSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Pasport
        fields = '__all__'
