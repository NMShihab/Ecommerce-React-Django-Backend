from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer,UserSerializerWithToken
from .models import User

@api_view(["GET"])
def getUserProfile(request):
    user = request.user 
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self,attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for key,value in serializer.items():
            data[key] = value

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


