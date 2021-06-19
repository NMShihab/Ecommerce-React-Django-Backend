from rest_framework import  serializers
from user.models import User
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= '__all__'