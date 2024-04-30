from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializers import *
from users.models import *

from .serializers import *
from .models import *

class TokenIntrospect(APIView):
    def post(self, request):
        return Response()
