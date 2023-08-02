from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *


# Create your views here.

def home(request):
    return HttpResponse("hello prakash")

@api_view(['GET'])
def getData(request):
    faebikes_obj = faebikes.objects.all()
    faebikes_Serializers = faebikesSerializers(faebikes_obj,many=True)
    return Response(faebikes_Serializers.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def postData(request):
    faebikes_Serializers = faebikesSerializers(data=request.data)
    if faebikes_Serializers.is_valid():
        faebikes_Serializers.save()

    
    return Response(faebikes_Serializers.data)

@api_view(['PUT'])
def updateData(request,pk):
    faebikes_obj = faebikes.objects.get(pk=pk)
    faebikes_Serializers = faebikesSerializers(instance=faebikes_obj,data=request.data)
    if faebikes_Serializers.is_valid():
        faebikes_Serializers.save()
    return Response(faebikes_Serializers.data)

@api_view(['DELETE'])
def delete(request,pk):
    faebikes_obj = faebikes.objects.get(pk=pk)
    faebikes_obj.delete()
    return Response("data was delete")
    
    