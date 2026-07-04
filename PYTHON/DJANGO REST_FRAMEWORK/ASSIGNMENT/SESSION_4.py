"""
Q1.Create a Django REST Framework API endpoint /api/playlists/ for a music app that is protected using BasicAuthentication. Only authenticated users should be able to view the list of playlists.
~~>
from rest_framework.generics import ListAPIView
from .models import Playlist
from .serializers import PlaylistSerializer

class PlaylistListView(ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer 
Ye SAbhi Record Ki List Return Karega Or Sirf GET Method Hi Handle Karta He Isme Sirf QuerySet Or Searializer Dene Par Automatically Wo PAgination,Ordering, And Fieltering Support Karta He.

Q2.Implement TokenAuthentication for a /api/orders/ endpoint in a Zomato-style food ordering app. Generate an auth token for a user using rest_framework.authtoken and test accessing the endpoint with and without the token.
~~>
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]

Url File Me :
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import OrderListView

urlpatterns = [
    path('api/orders/', OrderListView.as_view(), name='orders'),
    path('api/token/', obtain_auth_token, name='api-token'),
]

View Me :
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


Q3.Set up SessionAuthentication for a /api/cart/ endpoint in a Flipkart-style shopping app. Allow only logged-in users to add items to their cart, and return a 403 Forbidden error for unauthenticated users.<br><br><em><strong>Hint:</strong> Use the IsAuthenticated permission class.</em>
~~>
Model Me :
from django.db import models
class Cart(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product_name

View Me :

from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from .serializers import CartSerializer
class CartView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

ListCreateAPIView Ye DRF Me Sirf Data GET or POST Se Naya Data Add Karne Ke Liye Use Hota He.

Q4.Create a custom permission class IsPremiumUser for a BookMyShow-style ticket booking API. Only users with is_premium=True should be able to access /api/tickets/. Apply this permission to the view and test with both premium and non-premium users.
~~>
from rest_framework.permissions import BasePermission
class IsPremiumUser(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.is_premium
        )


from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication
from .models import Ticket
from .serializers import TicketSerializer
from .permissions import IsPremiumUser

class TicketListView(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsPremiumUser]


Q5.Use ChatGPT to explain the difference between TokenAuthentication and SessionAuthentication as if you are answering an interview question. Paste your answer in a text file named auth_comparison.txt.
~~>

Interview Answer: Difference between TokenAuthentication and SessionAuthentication

TokenAuthentication: - The server issues a unique token after login. -
The client sends the token in the Authorization header with every
request. - Commonly used for REST APIs, mobile apps, and single-page
applications. - Stateless: the server does not rely on a login session
for each request.

SessionAuthentication: - After login, Django creates a server-side
session and the browser stores a session cookie. - The browser
automatically sends the session cookie with future requests. - Best
suited for traditional web applications using Django templates. -
Stateful: the server keeps track of the user’s session.

Key Differences: 1. TokenAuthentication uses a token;
SessionAuthentication uses a session cookie. 2. TokenAuthentication is
ideal for APIs, mobile apps, and third-party clients. 3.
SessionAuthentication is ideal for browser-based Django websites. 4.
TokenAuthentication is stateless, while SessionAuthentication depends on
server-side sessions.

In short, I would choose TokenAuthentication for REST APIs consumed by
mobile or frontend apps, and SessionAuthentication for traditional
Django web applications where users log in through the website.







"""