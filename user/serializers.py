from rest_framework import  serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
    _id =  serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ('id','_id','email','name','username','isAdmin')
    
    def get_isAdmin(self,obj):
        return obj.is_staff
    def get__id(self,obj):
        return obj.id

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ('id','_id','email','name','username','isAdmin','token')
    
    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)