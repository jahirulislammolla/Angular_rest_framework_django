from django.shortcuts import render
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser,JSONParser
from .models import Laptop
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LaptopSerializer
from rest_framework import status
#initial show this page....
def home(request):
    return render(request,"home.html",{})
#create new laptop
@api_view(["POST"])
def laptopCreate(request):
    serializer=LaptopSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#update laptop value
@api_view(['POST'])
def laptopUpdate(request,pk):
    laptop=Laptop.objects.get(id=pk)
    serializer = LaptopSerializer(instance=laptop, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#show all laptop
@api_view(["GET"])
def laptopList(request):
    laptop=Laptop.objects.all()
    serializer=LaptopSerializer(laptop,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def laptopDetail(request,pk):
    laptop=Laptop.objects.get(id=pk)
    serializer=LaptopSerializer(laptop,many=False)
    return Response(serializer.data)
#delete laptop
@api_view(["DELETE"])
def laptopDelete(request,pk):
    laptop=Laptop.objects.get(id=pk)
    laptop.delete()
    return Response("Item delete successfully")