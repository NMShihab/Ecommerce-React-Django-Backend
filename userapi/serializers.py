from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ["id","username","email","name","_id","isAdmin"]
    
    def get_name(self,obj):
        name = obj.first_name

        if name == "":
            name = obj.email

        return name
    
    def get__id(self,obj):
        return obj.id

    def get_isAdmin(self,obj):
        return obj.is_staff


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email"]


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields =  ["id","username","email","name","_id","isAdmin","token"]

    def get_token(self,obj):
        token = RefreshToken.for_user(obj)

        return str(token.access_token)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for key,value in serializer.items():
            data[key] = value

        # data["id"] = self.user.id 
        # data["username"] = self.user.username 
        # data["email"] = self.user.email      

        return data