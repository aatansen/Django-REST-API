from rest_framework import serializers
from .models import Product_Model

class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Product_Model
        fields=['id','name','description','price']