from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from app.pasport.models import Pasport
from app.pasport.serializer import PasportSerializer


class GetPasport(APIView):
    def get_object(self, pk):
        try:
            return Pasport.objects.get(pk=pk)
        except Pasport.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        pasport = Pasport.objects.filter(user_id=request.user.id)[0]
        snippet = self.get_object(pk=pasport.id)
        serializer = PasportSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetListAllPasport(generics.ListAPIView):
    serializer_class = PasportSerializer

    def get_queryset(self):
        return Pasport.objects.all()