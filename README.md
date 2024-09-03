<div align="center">
<h1>Django REST API</h1>
</div>

## Context
- [Preparation](#preparation)
    - [Create virtual environment](#create-virtual-environment)
    - [Create new project](#create-new-project)
    - [Create new app](#create-new-app)
    - [`urls` and `views` setup inside app](#urls-and-views-setup-inside-app)
    - [Apply initial migrations](#apply-initial-migrations)
    - [Create and register model](#create-and-register-model)
    - [Create Superuser](#create-superuser)

### Preparation
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
