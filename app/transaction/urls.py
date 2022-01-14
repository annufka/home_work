from django.urls import path

from app.transaction.views import *

urlpatterns = [
    path('create/transaction/<str:token>/', CreateTransaction.as_view()),
    path('activate/transaction/<str:token>/<int:summ>/<int:code>/', ActivateTransaction.as_view()),
    path('search/music/', SearchDeezerMusic.as_view()),
]