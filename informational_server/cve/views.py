from rest_framework.views import APIView
from rest_framework.response import Response

import requests as r

class CVESearch(APIView):
    def get(self, request):
        query = request.GET.get('query', None)
        
