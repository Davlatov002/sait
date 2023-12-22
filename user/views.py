from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Profile
from rest_framework.response import Response
from rest_framework import status
from .serialazer import ProfileSerializer, ProfileLoginserialazer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

@swagger_auto_schema(method='POST', request_body=ProfileLoginserialazer, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get('email')
        password = request.data.get('password')
        try:
            profile = Profile.objects.get(email=username)
        except:
            try:
                profile = Profile.objects.get(username=username)
            except:
                return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)
        if profile:
            if profile.password == password:
                profile_serializer = ProfileSerializer(profile)
                return Response({'message': 1, "profile":profile_serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_profile(request):
    if request.method == 'GET':
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response({'message': 1,"profile":serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_profile_id(request, pk):
    if request.method == 'GET':
        profile = Profile.objects.get(id=pk)
        serializer = ProfileSerializer(profile)
        return Response({'message': 1,"profile":serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)
    