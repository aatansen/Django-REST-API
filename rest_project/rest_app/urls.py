from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('product_list/',product_list,name='product_list'),
    path('product/<pk>',product,name='product'),
]

urlpatterns=format_suffix_patterns(urlpatterns)