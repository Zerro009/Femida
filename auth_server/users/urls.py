from django.urls import path

from .views import *

urlpatterns = [
    path('', UserSignup.as_view(),),
    path('signin/', UserSignin.as_view(),),
]
