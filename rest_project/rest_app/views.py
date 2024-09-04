from django.shortcuts import render
from rest_framework.response import Response
from .models import Product_Model
from .serializers import Product_Serializer,Registration_Serializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
# Create your views here.

@api_view(['GET','POST'])
def product_list(request,format=None):
    if request.method == 'GET':
        # Retrieve all products from the database
        products = Product_Model.objects.all()
        # Serialize the product data
        serializer = Product_Serializer(products, many=True)
        # Return the serialized data as a response
        return Response(serializer.data)
    
    if request.method == 'POST':
        # Deserialize the request data
        serializer = Product_Serializer(data=request.data)
        # Validate the data
        if serializer.is_valid():
            # Save the data to the database
            serializer.save()
            # Return the serialized data as a response
            return Response(serializer.data)
        
@api_view(['GET','PUT','DELETE'])
def product(request,pk):
    try:
        # Attempt to retrieve the product from the database using the primary key
        product = Product_Model.objects.get(id=pk)
    except Product_Model.DoesNotExist:
        # Return a 404 Not Found response if the product does not exist
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # Serialize the product data
        serializer = Product_Serializer(product)
        # Return the serialized data as a response
        return Response(serializer.data)

    if request.method == 'PUT':
        # Deserialize the request data and update the product
        serializer = Product_Serializer(product, data=request.data)
        if serializer.is_valid():
            # Save the updated product data
            serializer.save()
            # Return the serialized updated product data as a response
            return Response(serializer.data)

    if request.method == 'DELETE':
        # Delete the product from the database
        product.delete()
        # Return a 204 No Content status
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        # Deserialize the request data into a Registration_Serializer
        serializer = Registration_Serializer(data=request.data)
        data = {}
        
        # Check if the serialized data is valid
        if serializer.is_valid():
            # Save the new user and add a success message to the response data
            user = serializer.save()
            data['response'] = 'Successfully registered a new user'
            
            # login 
            auth_token=Token.objects.get(user=user).key
            data['token']=auth_token
        else:
            # Add the serializer errors to the response data
            data = serializer.errors
        
        # Return the response data
        return Response(data)