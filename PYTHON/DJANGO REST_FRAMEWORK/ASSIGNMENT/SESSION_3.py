"""
Q1.Create a ModelViewSet for a Restaurant model (fields: name, cuisine, location) and register it with a DefaultRouter in your Django REST Framework project so that the API endpoints are automatically generated.
~~> 
from django.db import models
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.name

from rest_framework import serializers
from .models import Restaurant
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

from rest_framework.viewsets import ModelViewSet
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer()
        
Q2.Implement PageNumberPagination for your RestaurantViewSet so that the /api/restaurants/ endpoint returns only 3 restaurants per page.Set the pagination class and page size in your Django settings or directly in the viewset.
~~>
seting.py Me :
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 3,
}

from rest_framework.viewsets import ModelViewSet
from .models import Restaurant
from .serializers import RestaurantSerializer
from .pagination import RestaurantPagination

class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    pagination_class = RestaurantPagination

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


Q3.Switch your pagination to LimitOffsetPagination for the RestaurantViewSet and test the /api/restaurants/?limit=2&offset=2 endpoint to verify it returns the correct slice of restaurants.
~~>
pagination.oy Me:
from rest_framework.pagination import LimitOffsetPagination
class RestaurantPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10

view.py Me :
from .pagination import RestaurantPagination
class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    pagination_class = RestaurantPagination

Q4.Add ordering support to your RestaurantViewSet so users can order restaurants by name or cuisine using the ordering query parameter (e.g., /api/restaurants/?ordering=name or /api/restaurants/?ordering=-cuisine).
~~>
View.py Me :
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from .models import Restaurant
from .serializers import RestaurantSerializer
class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    pagination_class = LimitOffsetPagination

    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'cuisine']


Q5.Add a filter to your RestaurantViewSet so users can filter restaurants by cuisine type (e.g., /api/restaurants/?cuisine=Italian), and test it by creating at least two different cuisine types.<br><br><em><strong>Hint:</strong> Use DjangoFilterBackend and specify filterset_fields in your viewset.
~~>
DjangoFilterBackend  Ka Use Karke cuisin field  fileltering  Karke filter Karne ke Liye pip insatll django filter se third party modual import karna he
Uske Bad Apni Project Ke Seting.py Me : INSTALLED_APPS = [ 'django_filters',] Add Karo.

View Me :
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['cuisine']
    ordering_fields = ['name', 'cuisine']



""" 