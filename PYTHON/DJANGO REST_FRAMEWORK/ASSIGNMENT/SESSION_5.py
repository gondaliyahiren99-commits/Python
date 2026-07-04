"""
Q1.Create a Django REST Framework endpoint /api/music-weather/<city>/ that fetches the current weather for the given city using the OpenWeatherMap API and returns the temperature and weather description as JSON, as if you are showing weather info for a music festival app.
~~>
OpenWeatherMap API  Ke Use Karke Wether Fetch Karne Ke liye : pip install request
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

class MusicWeatherView(APIView):
    def get(self, request, city):
        url = (f"https://api.openweathermap.org/data/2.5/weather" f"?q={city}&appid={API_KEY}&units=metric")
        response = requests.get(url)
        if response.status_code != 200:
            return Response({"error": "City not found"},status=status.HTTP_404_NOT_FOUND)
        data = response.json()
        return Response({ "city": city,"temperature": data["main"]["temp"],"weather": data["weather"][0]["description"]})

Q2.Build a /api/food-location/ endpoint that takes a restaurant name as a query parameter, uses the Google Maps Geocoding API to find its latitude and longitude, and returns the coordinates in JSON.<br><br><em><strong>Hint:</strong> Use the requests library to call the external API and handle cases where the restaurant is not found.
~~>
Google Maps Geocoding API Ke Liye pip install requests module Install Karenge.
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"

class FoodLocationAPIView(APIView):
    def get(self, request):
        restaurant = request.query_params.get("restaurant")
        if not restaurant:
            return Response({"error": "Restaurant name is required."},status=status.HTTP_400_BAD_REQUEST)

        url = (
            f"https://maps.googleapis.com/maps/api/geocode/json"
            f"?address={restaurant}&key={API_KEY}"
        )

        response = requests.get(url)
        data = response.json()
        if data["status"] != "OK":
            return Response({"error": "Restaurant not found."},status=status.HTTP_404_NOT_FOUND)
        location = data["results"][0]["geometry"]["location"]
        return Response({ "restaurant": restaurant,"latitude": location["lat"],"longitude": location["lng"]})

Q3.Create a /api/country-info/<country_name>/ endpoint that uses the REST Countries API to fetch and return the population and capital of the given country, formatted as JSON, similar to how travel apps show quick country facts.
~~>
View Me :
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CountryInfoAPIView(APIView):
    def get(self, request, country_name):
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        response = requests.get(url)
        if response.status_code != 200:
            return Response({"error": "Country not found"},status=status.HTTP_404_NOT_FOUND)
        data = response.json()[0]
        return Response({"country": data["name"]["common"],"capital": data["capital"][0],"population": data["population"]})

Urls.py Me :
from django.urls import path
from .views import CountryInfoAPIView

urlpatterns = [
    path("api/country-info/<str:country_name>/",CountryInfoAPIView.as_view(),name="country-info"),
]


Q4.Use ChatGPT to generate a Python code snippet that sends a GET request to the GitHub API to fetch public repositories for a given username, then copy and adapt that code into a DRF view called /api/github-repos/<username>/ that returns the list of repository names as JSON.
~~>
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class GitHubReposAPIView(APIView):

    def get(self, request, username):
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url)
        if response.status_code != 200:
            return Response({"error": "GitHub user not found"},status=status.HTTP_404_NOT_FOUND)
        repos = response.json()
        repo_names = []
        for repo in repos:
            repo_names.append(repo["name"])
        return Response({"username": username,"repositories": repo_names})

"""