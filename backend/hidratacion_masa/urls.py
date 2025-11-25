from django.urls import path
from .views import CalculoHidratacionMasa

urlpatterns = [
    path('calcular-hidratacion/', CalculoHidratacionMasa.as_view() , name='hidratacion-masa'),
]
