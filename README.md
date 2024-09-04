<div align="center">
<h1>Django REST API</h1>
</div>

## Context
- [Preparation](#preparation)
    - [Package version](#package-version)
    - [Create virtual environment](#create-virtual-environment)
    - [Create new project](#create-new-project)
    - [Create new app](#create-new-app)
    - [`urls` and `views` setup inside app](#urls-and-views-setup-inside-app)
    - [Apply initial migrations](#apply-initial-migrations)
    - [Create and register model](#create-and-register-model)
    - [Create Superuser](#create-superuser)
- [Django Rest Framework CRUD Operation](#django-rest-framework-crud-operation)
    - [What is REST API](#what-is-rest-api)
    - [API application example](#api-application-example)
    - [Django Rest framework installation & setup](#django-rest-framework-installation--setup)
    - [Create a serializer](#create-a-serializer)
    - [Concent of serializer (Django)](#concent-of-serializer-django)
    - [HTTP methods](#http-methods)
    - [What is CRUD](#what-is-crud)
    - [Create (view endpoints/api endpoints) + GET request method](#create-view-endpointsapi-endpoints--get-request-method)
    - [Download and setup Postman](#download-and-setup-postman)
    - [GET request method in Postman](#get-request-method-in-postman)
    - [POST request method](#post-request-method)
    - [GET request - obtain a particular instance](#get-request---obtain-a-particular-instance)
    - [PUT request method](#put-request-method)
    - [DELETE request method](#delete-request-method)
    - [Obtaining JSON from browser](#obtaining-json-from-browser)
### Preparation
#### Package version
- Version of packages included in `requirements.txt`
#### Create virtual environment
- `py -m venv env`
- Activate environment `.\env\Scripts\activate`
- Install Django `pip install django`

[⬆️ Go to top](#context)

#### Create new project
- `django-admin startproject rest_project`
- Run the project `py manage.py runserver`

[⬆️ Go to top](#context)

#### Create new app
- `py manage.py startapp rest_app`
- Add app in `INSTALLED_APPS` inside `settings.py`

[⬆️ Go to top](#context)

#### `urls` and `views` setup inside app
- `views.py` already present inside `rest_app`
- Create `urls.py` in `rest_app`
    ```py
    from django.urls import path
    from .views import *

    urlpatterns=[
        
    ]
    ```
- Now include it in project `urls.py`
    ```py 
    from django.contrib import admin
    from django.urls import path,include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',include('rest_app.urls'))
    ]
    ```

[⬆️ Go to top](#context)

#### Apply initial migrations
- `py manage.py migrate`

[⬆️ Go to top](#context)

#### Create and register model
- Create model in `models.py`
    ```py
    from django.db import models

    # Create your models here.
    class Product_Model(models.Model):
        name=models.CharField(max_length=200)
        description=models.CharField(max_length=200)
        description=models.CharField(max_length=600)
        price=models.DecimalField(max_digits=4,decimal_places=2)
        def __str__(self):
            return self.name
    ```
- Register model in `admin.py`
    ```py
    from django.contrib import admin
    from .models import *

    # Register your models here.
    admin.site.register(Product_Model)
    ```
- Migrate model
    - `py manage.py makemigrations`
    - `py manage.py migrate`

[⬆️ Go to top](#context)

#### Create Superuser
- To view model data we will create superuser
    `py manage.py createsuperuser`
    > fill up prompted field data

[⬆️ Go to top](#context)

### Django Rest Framework CRUD Operation
#### What is REST API
- API stands for application programming interface
- An API is a unique way of saying how two pieces of software can communicate with one another
- It effectively allows different applications that are written in different languages to communicate with each other
- The ‘REST’ part describes how the API is communicating 
- If the API is making use of ‘REST’ then our API is communicating over standard web
requests

[⬆️ Go to top](#context)

#### API application example
- JSON is the language of communication
- The API describes what we want to communicate
- Examples of API uses may include:
    - Getting a list of users in an application
    - Deleting a particular user
    - Updating user profile information
- API endpoints occur once we make a request to the server
- Diagram of React(Frontend) & Django(Backend) API
    ```mermaid
    sequenceDiagram
        participant R as React Frontend
        participant D as Django Backend

        R->>D: Send JSON Request (e.g., GET /api/data)
        D->>D: Process Request
        D->>R: Send JSON Response (e.g., { "data": "value" })
        R->>R: Process JSON Response
        R->>D: Send JSON Request (e.g., POST /api/submit)
        D->>D: Process Data
        D->>R: Send Confirmation Response (e.g., { "status": "success" })
        R->>R: Update UI Based on Confirmation
    ```
- Diagram of React(Frontend) , Django(Backend) API & PostgreSQL(Database)
    ```mermaid
    sequenceDiagram
        participant R as React Frontend
        participant D as Django Backend
        participant DB as PostgreSQL Database

        R->>D: Send JSON Request (e.g., GET /api/data)
        D->>DB: Query Data (e.g., SELECT * FROM table)
        DB->>D: Return Data (e.g., { "data": "value" })
        D->>R: Send JSON Response (e.g., { "data": "value" })
        R->>R: Process JSON Response

        R->>D: Send JSON Request (e.g., POST /api/submit)
        D->>DB: Insert/Update Data (e.g., INSERT INTO table (column) VALUES (value))
        DB->>D: Confirmation (e.g., { "status": "success" })
        D->>R: Send Confirmation Response (e.g., { "status": "success" })
        R->>R: Update UI Based on Confirmation
    ```

[⬆️ Go to top](#context)

#### Django Rest framework installation & setup
- `pip install djangorestframework`
- Add `rest_framework` in `INSTALLED_APPS`
    ```py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_app',
        'rest_framework',
    ]
    ```

[⬆️ Go to top](#context)

#### Create a serializer
- Create a file `serializers.py` inside app directory and create a class as below
    ```py
    from rest_framework import serializers
    from .models import Product_Model

    class Product_Serializer(serializers.ModelSerializer):
        class Meta:
            model=Product_Model
            fields=['id','name','description','price']
    ```

[⬆️ Go to top](#context)

#### Concent of serializer (Django)
- A serializer is a component used in the DRF (Django Rest Framework) to translate a
Python object into a JSON format
- A diagram to visualize serializer
    ```mermaid
    sequenceDiagram
        participant C as Client
        participant D as Django
        participant S as Serializer
        participant DB as Database

        C->>D: Send Request (e.g., POST /api/data with JSON payload)
        D->>S: Instantiate Serializer with Data
        S->>S: Validate Data
        alt Validation Successful
            S->>DB: Save Validated Data
            DB->>S: Confirmation (e.g., { "status": "success" })
            S->>D: Return Processed Data (e.g., Serialized Response)
        else Validation Failed
            S->>D: Return Validation Errors (e.g., { "errors": "detail" })
        end
        D->>C: Send Response (e.g., JSON with data or errors)
    ```

[⬆️ Go to top](#context)

#### HTTP methods
All API viewpoints are based on certain API methods, which include:
- GET (obtain/retrieve data)
- POST (create or send data)
- PUT (Update and replace current data)
- DELETE (remove data)

[⬆️ Go to top](#context)

#### What is CRUD
- CRUD involves a set of functions that need to be carried out by a database
- These functions include:
    - CREATE --> POST request (HTTP method)
    - READ --> GET request (HTTP method)
    - UPDATE --> PUT request (HTTP method)
    - DELETE --> DELETE request (HTTP method)

[⬆️ Go to top](#context)

#### Create (view endpoints/api endpoints) + GET request method
- Create a function in views
    ```py
    from django.shortcuts import render
    from rest_framework.response import Response
    from .models import Product_Model
    from .serializers import Product_Serializer
    from rest_framework.decorators import api_view
    # Create your views here.

    @api_view(['GET'])
    def product_list(request):
        if request.method=='GET':
            # get all product list 
            products=Product_Model.objects.all()
            serializer=Product_Serializer(products,many=True)
            return Response(serializer.data)
    ```
    - Here we get everything from the `Product_Model` model and convert it into serializer JSON format
    - `from rest_framework.response import Response` is used for json formatted response provided by REST framework also a nice looking interface
    - `from rest_framework.decorators import api_view` is used for make use of `GET` request
- Create url path to view 
    ```py
    from django.urls import path
    from .views import *

    urlpatterns=[
        path('product_list/',product_list,name='product_list')
    ]
    ```
[⬆️ Go to top](#context)

#### Download and setup Postman
- Download [Postman](https://www.postman.com/downloads/)
- Setup and login

[⬆️ Go to top](#context)

#### GET request method in Postman
- Open Postman
- Click new and select `HTTP request`
- Select `GET` and provide url `http://127.0.0.1:8000/product_list/`

[⬆️ Go to top](#context)

#### POST request method
- We will make POST request in same function as GET request; update `product_list` function with POST method
    ```py
    @api_view(['GET','POST'])
    def product_list(request):
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
    ```
- Now in Postman using the same url `http://127.0.0.1:8000/product_list/` and select `POST`
- Select `body` then select `raw` and `json` format
    ```json
    {
        "name":"Fanta",
        "description":"Juice",
        "price":"5.99"
    }
    ```
- Now click `Send`

[⬆️ Go to top](#context)

#### GET request - obtain a particular instance
- Create new function for getting particular instance
    ```py
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
    ```
- In `urls.py` add new path `path('product/<pk>',product,name='product')`
- Now `http://127.0.0.1:8000/product/1` will get the particular data

[⬆️ Go to top](#context)

#### PUT request method
- It is update/replace method
- Check request and update product in `product` function
    ```py
    if request.method == 'PUT':
        # Deserialize the request data and update the product
        serializer = Product_Serializer(product, data=request.data)
        if serializer.is_valid():
            # Save the updated product data
            serializer.save()
            # Return the serialized updated product data as a response
            return Response(serializer.data)
    ```
    - Here `product` in deserialize is `product = Product_Model.objects.get(id=pk)`

[⬆️ Go to top](#context)

#### DELETE request method
- Check request and delete product in `product` function
    ```py
    if request.method == 'DELETE':
        # Delete the product from the database
        product.delete()
        # Return a 204 No Content status
        return Response(status=status.HTTP_204_NO_CONTENT)
    ```
    - Here `product` is `product = Product_Model.objects.get(id=pk)`

[⬆️ Go to top](#context)

#### Obtaining JSON from browser
- In `urls.py` import `from rest_framework.urlpatterns import format_suffix_patterns`
- Now use the method `urlpatterns=format_suffix_patterns(urlpatterns)`
- In `views.py` add `format=None` in `product_list` function
- Now in browser view the JSON in `http://127.0.0.1:8000/product_list.json`

[⬆️ Go to top](#context)