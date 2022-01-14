from django.urls import path

from app.profile.views import CreateProfileFirst, CreateProfile, GetListProfiles, PatchProfile

urlpatterns = [
    path('create/profile/first/', CreateProfileFirst.as_view()),
    path('create/profile/', CreateProfile.as_view()),
    path('get/all/profiles/', GetListProfiles.as_view()),
    path('patch/profile/<int:pk>/', PatchProfile.as_view()),
    ]