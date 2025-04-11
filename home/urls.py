from django.urls import path
from home.views import inicio, crear_auto

urlpatterns = [
    path('', inicio, name='inicio'),
    path('autos/crear/', crear_auto, name='crear_auto'),
]
