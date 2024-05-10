from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# logic for get data
@api_view(['GET'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

# logic for create task data
@api_view(['POST'])
def task_create(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
           return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# logic for update data
@api_view(['GET', 'PUT'])
def task_update(request, id):
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response(status=404)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

# logic for delete data
@api_view(['GET','DELETE'])    
def task_delete(request, id):   
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response(status=404)  
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)      
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=204)         
