from django.urls import path, re_path

from App.views.register import RegisterAPI
from App.views.login import LoginAPI
from App.views.updateprofile import UpdateProfile

urlpatterns = [
 path('register', RegisterAPI.as_view()),
 path('login', LoginAPI.as_view()),
 path('updateprofile', UpdateProfile.as_view()),

]
