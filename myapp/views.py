from rest_framework.views import APIView
from rest_framework.response import Response
from .service import get_greeting

class GreetView(APIView):
    def get(self, request):
        name = request.GET.get('name')
        return Response(get_greeting(name))
