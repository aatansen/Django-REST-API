from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('product_list/',product_list,name='product_list'),
    path('product/<pk>',product,name='product'),
    path('register/',register,name='register'),
    path('login/',obtain_auth_token,name='login'),
]

urlpatterns=format_suffix_patterns(urlpatterns)