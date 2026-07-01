from django.shortcuts import render
from django.http import HTTpResponce

# Create your views here.
def login(request):
    return(request,'jobseeker/login.html')

def register(request):
    return(request,'jobseeker/register.html')