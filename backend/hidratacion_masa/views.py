from rest_framework.views import APIView

from .serializers import HidratacionMasaSerializer
# Create your views here.

class CalculoHidratacionMasa(APIView):
    """
    Calcula la hidratacion de la masa.
    """
    
    def post(self, request):
        serializer = HidratacionMasaSerializer(data=request.data)