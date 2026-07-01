from django.shortcuts import render
# pyrefly: ignore [missing-import]
from .forms import AddRestaurant

# Create your views here.
def add_restaurant(request):
    form=AddRestaurant()
    context={
        'page_title':"Add Restaurant",
        'form':form
        }
    return render(request,'my_app/add_restaurant.html',context)