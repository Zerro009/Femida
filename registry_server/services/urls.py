from django.urls import path

from .views import *

urlpatterns = [
    path('', ServiceList.as_view()),
    path('detail/', ServiceDetail.as_view())
]
