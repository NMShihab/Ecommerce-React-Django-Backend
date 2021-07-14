from django.shortcuts import render
from django.http import JsonResponse, response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import MyTokenObtainPairSerializer, UserSerializer,UserDataSerializer,UserSerializerWithToken



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def userRegister(request):
    data = request.data

    try:
        user = User.objects.create(
            first_name = data['name'],
            username = data['email'],
            email = data['email'],
            password = make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user,many=False)
        return Response(serializer.data)
    except:
        message = {"details":"user with this email already exist"}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user,many=False)

    data = request.data
    
    user.first_name = data['name']  
    user.username = data['email']
    user.email = data['email']    

    if data['password'] != "":
        user.password = make_password(data['password'])

    user.save()

    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
def getAllProfile(request):
    users = User.objects.all()
    serializer = UserDataSerializer(users,many=True)
    return Response(serializer.data)



