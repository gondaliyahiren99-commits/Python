from my_app.models import Resturant_admin
from my_app.models import Restaurant
from my_app.models import Cuisine
from django.contrib import admin

# Register your models here.
admin.site.register(Cuisine)
# admin.site.register(Restaurant)
admin.site.register(Restaurant, Resturant_admin)
