"""
Q1.Install Django and Django REST Framework in a new virtual environment, then create a Django project named foodiehub and an app named api.
~~> Apne Enviournment Ke Specific Location par Usko Activate Karke Us ko close karenge. Bad Me pip install djangorestframework Command Do. Uske Bad Project ke Folder Me App Create Karo Jiska Name api Rakho. Us App Ko Seting.py Ke Installed App Me Add Karo. Waha python manage.py runserver Command chalao. Abhi Admin Panell Banaya Nahi To Koi Project Ya App Show Nahi Hoga.

Q2.Add 'rest_framework' to the INSTALLED_APPS list in your foodiehub/settings.py file and verify the app runs without errors by starting the development server.
~~> Browser Me URL Search Karo http://127.0.0.1:8000/ .Agar Koi Error NAhi Aye To Sahi Se Work Kar Raha He.

Q3.Create a new file views.py inside your api app and build a function-based API endpoint hello_spotify that returns JSON: {"message": "Hello, Spotify Fans!"} when accessed at /api/hello_spotify/.
~~>    
from django.http import JsonResponse
def hello_spotify(request):
    return JsonResponse({"message": "Hello, Spotify Fans!"})

Q5.Use ChatGPT or Copilot to help you write a basic Serializer class in serializers.py for a Zomato-style Restaurant object with fields: name and cuisine. Paste your serializer code and mention what prompt you gave the AI tool.
~~>
from rest_framework import serializers
from .models import Restaurant
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'cuisine']
        
AI Tool : ChatGPT
"""