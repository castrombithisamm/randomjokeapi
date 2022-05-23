import imp
from os import stat
import re
from urllib import response
from xmlrpc.client import ResponseError
from django.http import JsonResponse
from .models import DryJoke
from .serializers import DryJokeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from jokes import serializers

@api_view(['GET', 'POST'])
def joke_list(request, format=None):


    #get all the jokes
    #serialize them
    #return json
    if request.method == 'GET':
        dryjokes = DryJoke.objects.all()
        serializer = DryJokeSerializer(dryjokes, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer =  DryJokeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])            
def joke_detail(request, id, format=None):

    try:     
        dryjoke =  DryJoke.objects.get(pk=id)
    except DryJoke.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DryJokeSerializer(dryjoke)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DryJokeSerializer(dryjoke,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        dryjoke.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
