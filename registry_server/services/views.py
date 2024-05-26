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
        service = None
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            service = serializer.save()
            routes = request.data['routes']
            for route in routes:
                Route.objects.update_or_create(service=service, path=route['path'])
            return Response(status=201)
        return Response(status=400)

class ServiceDetail(APIView):
    def get(self, request):
        path = request.GET.get('path', None)
        for i in Route.objects.all():
            print(i.path)
        if not path:
            return Response(status=400)
        try:
            route = Route.objects.get(path=path)
            service = route.service
            serializer = ServiceSerializer(service)
            return Response(serializer.data)
        except Route.DoesNotExist:
            return Response(status=404)
