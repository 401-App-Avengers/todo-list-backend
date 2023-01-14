from django.shortcuts import render
from rest_framework import viewsets, views, response, status
from .serializers import TodoSerializer
from .models import TodoItem
from .serializers import TodoSerializer

# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = TodoItem.objects.all()