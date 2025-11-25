from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HidratacionMasaSerializer
# Create your views here.

class CalculoHidratacionMasa(APIView):
    """
    Calcula la hidratacion de la masa.
    """
    
    def post(self, request):
        serializer = HidratacionMasaSerializer(data=request.data)
        
        if serializer.is_valid():
            cantidad_harina = serializer.validated_data['cantidad_harina']
            cantidad_agua = serializer.validated_data['cantidad_agua']
            
            hidratacion = (cantidad_agua / cantidad_harina) * 100
            
            return Response(
                {
                    "hidratacion": hidratacion,
                    "detalle": {
                        "Harina total": cantidad_harina,
                        "Agua total": cantidad_agua,
                    }
                },
                status=status.HTTP_200_OK
            )