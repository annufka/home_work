from django.urls import path

from app.pasport.views import GetPasport, GetListAllPasport

urlpatterns = [
    path('get/pasport/by/token/', GetPasport.as_view()),
    path('get/list/all/pasport/', GetListAllPasport.as_view()),
]