""".
Q1.Set up a Django REST Framework endpoint called /api/send-email/ that sends a welcome email to a user using the Mailgun API when a POST request is made with the user's email address.Use the requests library to call Mailgun's API from your Django view.</em>
~~>
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


MAILGUN_API_KEY = "YOUR_MAILGUN_API_KEY"
MAILGUN_DOMAIN = "YOUR_MAILGUN_DOMAIN"

class SendEmailAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response({"error": "Email is required"},status=status.HTTP_400_BAD_REQUEST)

        response = requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
            auth=("api", MAILGUN_API_KEY),
            data={
                "from": f"Welcome <mailgun@{MAILGUN_DOMAIN}>",
                "to": email,
                "subject": "Welcome to Our App",
                "text": "Welcome! Thank you for joining our application."
            }
        )

        if response.status_code == 200:
            return Response({"message": "Welcome email sent successfully"},status=status.HTTP_200_OK)

        return Response({"error": "Failed to send email","details": response.text},status=status.HTTP_400_BAD_REQUEST)

Q2.Create a /api/send-sms/ endpoint that accepts a phone number and message, then sends the SMS using Twilio's API. Register for a free Twilio account to get test credentials and use the twilio Python package.
~~>
pip install twilio


URL File Me :
from django.urls import path
from .views import SendSMSAPIView

urlpatterns = [
    path("api/send-sms/",SendSMSAPIView.as_view(),name="send-sms",),
]
 View Me :
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from twilio.rest import Client


ACCOUNT_SID = "YOUR_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_AUTH_TOKEN"
TWILIO_PHONE_NUMBER = "+1234567890"


class SendSMSAPIView(APIView):
    def post(self, request):
        phone = request.data.get("phone")
        message = request.data.get("message")
        if not phone or not message:
            return Response({"error": "Phone number and message are required."},status=status.HTTP_400_BAD_REQUEST)

        try:
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            sms = client.messages.create(body=message,from_=TWILIO_PHONE_NUMBER,to=phone)
            return Response(
                {"message": "SMS sent successfully","sid": sms.sid},status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)},status=status.HTTP_400_BAD_REQUEST)


Q3.Add a /api/pay/ endpoint that simulates a payment using Stripe's test API keys — accept amount and currency in the POST body and return a custom JSON response with payment status and transaction ID.
~~>
pip install stripe

import stripe

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

stripe.api_key = "sk_test_your_secret_key"


class PaymentAPIView(APIView):
    def post(self, request):
        amount = request.data.get("amount")
        currency = request.data.get("currency")
        if not amount or not currency:
            return Response({"error": "Amount and currency are required."},status=status.HTTP_400_BAD_REQUEST)
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=int(amount),
                currency=currency,
                payment_method_types=["card"]
            )
            return Response(
                {"status": "success","transaction_id": payment_intent.id,"amount": payment_intent.amount,"currency": payment_intent.currency},
                status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "failed","error": str(e)},status=status.HTTP_400_BAD_REQUEST)


Q4.Implement Google Login for your Django REST API so users can authenticate using their Google account and receive a JWT token.Use the django-allauth or social-auth-app-django package for social authentication integration.
~~>
pip install django-allauth
pip install dj-rest-auth
pip install djangorestframework-simplejwt

uske Bad Setinng.py Me:
INSTALLED_APPS = [
    ...
    "django.contrib.sites",
    "rest_framework",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "dj_rest_auth",
]
SITE_ID = 1

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": "YOUR_GOOGLE_CLIENT_ID",
            "secret": "YOUR_GOOGLE_CLIENT_SECRET",
            "key": ""
        }
    }
}

from django.urls import path, include

urlpatterns = [
    path("api/", include("dj_rest_auth.urls")),
    path("accounts/", include("allauth.urls")),
]


Q5.Deploy your Django REST API to PythonAnywhere and verify that the /api/send-email/ endpoint works live by testing it with Postman. Include a screenshot of your live endpoint response in your submission.
~~>
1.Create a free account on PythonAnywhere.
2.Upload your Django project (or clone it from GitHub).
3.Create a virtual environment:
4.python3 -m venv venv
5.venv.scripts/activate
6.Install project dependencies:
    pip install -r requirements.txt
8.Run database migrations:
9.python manage.py migrate
10.Collect static files:
    python manage.py collectstatic
11.Go to the Web tab and create a new web app.
12.Configure the WSGI file to point to your Django project.
13.Add your project path and virtual environment path in the Web tab.
14.Reload the web application.
15.Open your live URL:
    https://yourusername.pythonanywhere.com/
16.Test the endpoint in Postman:
    POST https://yourusername.pythonanywhere.com/api/send-email/
17.Set the header:
    Content-Type: application/json
18.Send the request body:
    {
        "email": "test@example.com"
    }
19.Verify that the API returns a success response.
"""