
from my_app.models import Restaurant
from my_app.models import Cuisine
from django.contrib import admin

# # Register your models here.
# admin.site.register(Cuisine)
# # admin.site.register(Restaurant)
# admin.site.register(Restaurant, Resturant_admin)
from django.contrib import admin
from .models import Restaurant, Cuisine

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'location', 'cuisine')
    search_fields = ('name', 'location')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Cuisine)