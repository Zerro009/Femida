from django.urls import path

from .views import *

urlpatterns = [
    path('introspect/', TokenIntrospect.as_view()),
]
