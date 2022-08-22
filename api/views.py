from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.http import JsonResponse 
from .models import Todo
from . import serializers

@api_view(['GET'])
def home(request):
    return Response({"Hello  kiash give as the api now my app is now working"})

@api_view(['GET'])
def Todoview(request):
    todos = Todo.objects.all()
    serializer =serializers.TodoSerializer(todos, many=True)
    return Response(serializer.data)