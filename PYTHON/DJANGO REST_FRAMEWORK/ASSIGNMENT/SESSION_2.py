"""
Q1. Create a Django model called Restaurant with fields name, cuisine, and rating, then register it in the admin panel.
~~> 
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField()
    def __str__(self):
        return self.name

    Model Crete Ke  Bad Model Ko admin.py File Me Model Ko Register Kar Ke Usko Makemigration or Migrate Karo.

Q2.Write a ModelSerializer named RestaurantSerializer for the Restaurant model to convert model instances to JSON and vice versa.
Use serializers.ModelSerializer and define the Meta class inside your serializer.
~~>
Apne Project Me File serializer.py Name Ki File Create Karte He.Uske Andar Searializer Create Karte He.
from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'cuisine', 'rating']

    -Ye Batata He Ki KOnsa Model Ke Data Or Us Model Ki Konsi Fields Use Karni He.

Q3.Build CRUD API endpoints for the Restaurant model using Django REST Framework's APIView class: implement POST to add a new restaurant, GET to list all restaurants, PUT/PATCH to update a restaurant by id, and DELETE to remove a restaurant by id.
~~>
# App Ki urls.py Me :
from django.urls import path
from .views import RestaurantAPIView, RestaurantDetailAPIView

urlpatterns = [
    path('restaurants/', RestaurantAPIView.as_view()),
    path('restaurants/<int:id>/', RestaurantDetailAPIView.as_view()),
]

# View Me :
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantAPIView(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetailAPIView(APIView):
    def put(self, request, id):
        restaurant = Restaurant.objects.get(id=id)
        serializer = RestaurantSerializer(restaurant, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, id):
        restaurant = Restaurant.objects.get(id=id)

        serializer = RestaurantSerializer(restaurant,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        restaurant = Restaurant.objects.get(id=id)
        restaurant.delete()

        return Response(
            {"message": "Restaurant Deleted Successfully"},
            status=status.HTTP_204_NO_CONTENT
        )


Q5.Use the GenericAPIView and mixins to refactor your Restaurant API so that listing, creating, updating, and deleting restaurants require less boilerplate code.
from rest_framework import mixins, generics
from .models import Restaurant
from .serializers import RestaurantSerializer


# List + Create
class RestaurantListCreateAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


# Update + Delete
class RestaurantDetailAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = "id"

    def put(self, request, id):
        return self.update(request, id=id)

    def patch(self, request, id):
        return self.partial_update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)
        
        
"""