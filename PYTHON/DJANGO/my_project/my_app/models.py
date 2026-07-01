from django.contrib import admin
from django.db import models

# Create your models here.


class Cuisine(models.Model):
    name=models.CharField(max_length = 30)
    description=models.TextField()

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name=models.CharField(max_length = 30,unique=True)
    location=models.CharField(max_length = 30)
    rating=models.FloatField()
    cuisine = models.ForeignKey(Cuisine,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Resturant_admin(admin.ModelAdmin):
    list_display = ('name','rating','location','cuisine')
    search_fields = ('name', 'location')
