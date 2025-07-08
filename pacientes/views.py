from rest_framework import viewsets
from .models import Paciente
from .serializers import PacienteSerializer
from django.shortcuts import render

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

def index(request):
    return render(request, 'index.html')
