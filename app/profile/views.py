from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from app.profile.models import Profile
from app.profile.serializer import CreateProfileFirstSerializer, CreateProfileSerializer, ProfileSerializer


class CreateProfileFirst(APIView):

    def post(self, request, format=None):
        serializer = CreateProfileFirstSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.create_user(request.data["username"], request.data["email"], request.data["password"], is_staff=True)
            user.save()
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateProfile(APIView):

    def post(self, request, format=None):
        serializer = CreateProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetListProfiles(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()

class PatchProfile(APIView):

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProfileSerializer(snippet)
        return Response(serializer.data)

    def patch(self, request, pk):
        object = self.get_object(pk)
        serializer = CreateProfileSerializer(object, data=request.data,
                                         partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)