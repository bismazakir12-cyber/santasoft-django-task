from rest_framework.decorators import api_view
from rest_framework.response import Response
from .service import get_greeting

@api_view(['GET'])
def greet(request):
    name = request.GET.get('name')
    return Response(get_greeting(name))
