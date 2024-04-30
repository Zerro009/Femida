from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password

from tokens.serializers import *
from tokens.models import *

from .serializers import *
from .models import *

class UserSignup(APIView):
    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
            return Response(status=201)
        print(serializer.errors)
        return Response(status=400)

class UserSignin(APIView):
    def post(self, request):
        user = None
        if User.objects.filter(username=request.data['username']).exists():
            user = User.objects.get(username=request.data['username'])
            if user.check_password(request.data['password']):
                return Response()
        return Response(status=400)
