from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.http import JsonResponse 
from .models import Todo
from .serialaizers import TodoSerializer
@api_view(['GET'])
def Todoview(request):
    todos = Todo.objects.all()
    serializer =TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TodoDetail(request,pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def TodoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def TodoUpdate(request,pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])

def TodoDelete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response("Item succesfully deleted")