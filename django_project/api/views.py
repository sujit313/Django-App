from rest_framework import viewsets
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from django.http import HttpResponse
from django.shortcuts import render

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

def home(request):
    return render(request, 'home.html')