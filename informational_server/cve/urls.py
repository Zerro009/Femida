from django.urls import path

from .views import *

urlpatterns = [
    path('search/', CVESearch.as_view()),
]
