
from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_votante, name='votante_api'),  
    path('candidato/', views.registrar_candidato, name='candidato_api'),
]