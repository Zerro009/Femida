from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *

class ServiceList(APIView):
    def get(self, request):
        instances = Service.objects.all()
        serializer = ServiceSerializer(instances, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['host'] = request.META['REMOTE_ADDR']
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        print(serializer.errors)
        return Response(status=400)
