import random
import string
from datetime import datetime

import requests
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.pasport.models import Pasport
from app.transaction.models import Transaction, Music
from app.transaction.serializer import TransactionSerializer

def code_generator(size=8, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class CreateTransaction(APIView):
    def post(self, request, token,  format=None):
        user = User.objects.filter(auth_token=token)[0]

        #генерируем случайный код для дальнейшей проверки трансакции
        code = code_generator()

        #создадим запись о трансакции
        about_transaction = {"code": code}
        serializer = TransactionSerializer(data=about_transaction)
        if serializer.is_valid():
            serializer.save(user_id=user.id)

        send_mail(
                "Подтвердите трансакцию",
                "Перейдите по ссылке http://127.0.0.1:8000/api/v1/transaction/activate/transaction/" + token + "/" + str(request.data.get("summ")) + "/" + str(code) + "/",
                'brilchem@gmail.com',
                [user.email],
        )
        return Response("Transaction is success", status=status.HTTP_201_CREATED)

class ActivateTransaction(APIView):
     def get(self, request, token, summ, code, format=None):
         Transaction.objects.filter(code=code).update(summ=summ)
         Transaction.objects.filter(code=code).update(code=0)
         user = User.objects.filter(auth_token=token)[0]
         Pasport.objects.filter(user = user).update(balance=summ)
         return Response("Ok", status=status.HTTP_200_OK)

class SearchDeezerMusic(APIView):
    def post(self, request, format=None):
        responce = requests.get("https://api.deezer.com/search?q={}".format(request.data.get("singer")))
        song_list = responce.json()
        #{"singer":"Epolets"}
        for item in song_list['data']:
            new_song = Music(singer=str(item['artist']['name']), song=str(item['title_short']), data_type=datetime.now())
            new_song.save()
        return Response("OK", status=status.HTTP_201_CREATED)