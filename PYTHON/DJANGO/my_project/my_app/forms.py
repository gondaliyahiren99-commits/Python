from django import forms

class AddRestaurant(forms.Form):
    restaturant_name=forms.CharField(max_length=30,label="Restaurant Name")
    cuisine_type = forms.CharField(max_length=30,label="Cuisine Type")
    contact_email=forms.EmailField(label="Contact EMail")