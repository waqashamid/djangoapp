from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def gettingstarted(request):
    return Response(data={"message" : "Hello BKL!"})