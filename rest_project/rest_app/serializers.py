from rest_framework import serializers
from .models import Product_Model
from django.contrib.auth.models import User

class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Product_Model
        fields=['id','name','description','price']
        
class Registration_Serializer(serializers.ModelSerializer):
    password2=serializers.CharField(
        style={'input_type':'password'},
        write_only=True,
        required=True,
    )
    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        
        if password!=password2:
            raise serializers.ValidationError({'password':'Sorry,password did not matched'})
        
        user.set_password(password)
        user.save()
        return user