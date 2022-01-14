from djoser.serializers import UserSerializer
from rest_framework import serializers

from app.profile.models import ProfileFirst, Profile


class CreateProfileFirstSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileFirst
        fields = '__all__'

class CreateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Profile
        fields = ["user", "first_name"]