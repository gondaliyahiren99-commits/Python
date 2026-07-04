"""                                     
                                                        *=*=*=*= Section A: Conceptual Understanding  *=*=*=*=

Q1. Explain the Django Request-Response cycle and how it differs from a standardPython script execution.
~~> 
STEP:
    1. User Koi Browser me Koi Request Send Karat He To Browser Server Ko Http Request Send krata He.
    2. Django Ka server Ye request Receive Karta he.
    3. Requset Me jo bhi Url Mili He Usme Check Karega Ki Konse App Ki Konsi Url.py me jana he.
    4. Waha Par Url Me Jo Bhi Views Diya he Uske View.py file me Jakar Function Run karke Usme Process Karega.
    5. Function Me ORM ki help se Model.py me Jo Bhi Database Banaya He Usme Data Fetch , Read , Add Karenge.
    6. Agar HTML ke PAge Se DAta Aa raha he to Wo Data Ko Python Object me Convert karega or Python Object Se Koi Specific Databasse Me Save Karega. Agar nahi Mil Raha He TO Usko HTML Page render Kar Dege.

Q2. Explain why Django Model Fields (CharField, IntegerField) are more robust for
profile data than Python dynamic typing.
~~> Django model Me Fields Me CharField Se Jyada IntegerField Jayada Effective Kyuki Agar Hume Koi Fields Me Integer Data Store Karna He To IntegerField Karna Padega Or Agar Galtu Se Usme CharField Dal Ne Ki KOshish Ki To Wo Error De Dega.Lekin Agar Usme CharFields Di To Wo Koi Bhi Value Do Vo String Form Me Save KArega Or Koi Error Nahi Dega.

Q3. Explain how Django Forms handle automated input validation for usernames and age ranges.
~~> Django  Inbuit System Validation Provide Karta He jisme USer Submit Karta he To Wo Check Karta He Ki User Ne Bheja Data Sahi He Ya Nahi Agar Data Galat Hoga To Wahi Error Dega Aur Usko Datavase Me SAve Hi Nahi Hone Deta.
    
Q4. Explain how to implement conditional logic in Django Templates to toggle account visibility.
~~>  Jab Programer ko Dikhana Ek hi Chhez Do Alag-Alag Form Dikhani Ho To Condionin Lagate He. eg. Agar User Ka Gender Male He YA Female Ke Hisab Se USki Default Profile Show Karna. 
5. Explain the difference between iterating through a Python list and a Django QuerySet.
~~>  Python list Jo Database Se Connect Nahi Hota Yani Wo sirf Huamara Programe Run Hoga tAb Tak Hi Exist KArega Programe Khatam Hone Ke Bad Automaticaly Destroy Hoga Ye Static Data Hi Dega jO List Create Time Diya Hota He. Jab Django QuerySet Ye Database Se Connect Hota He. Databasse se Data Fetch , Add , Crete Yea Delete Karta He.

6. Explain why the Django ORM is preferred over Python dictionaries for persistent profile storage. 
~~> Django ORM Ko python Dictionary Se Jyada Prefer Kiya Jata He kyunki Dictinary Ka Data RAM Me Store Hota He Jo Programe Close Hone Ke Bad Automatically Destroy Hoga.
Jab ORM ka Data DAtabase Me Permenatly Data Store Karta He.Large Data Ko Automaticaly Manage Karta He Aur Time Save Hota he Jab Dictionary Me Data LArge Scale Me 
DatavSave Karna Posible Nahi He.
                                                
                                                                *=*=*=*= Section B: Practical Ta  *=*=*=*=                                                             """
                                         
"""
P1. Define UserProfile Model: Create a class in models.py inheriting from models.Model. Define fields such as CharField for the username,IntegerField for age, and
BooleanField for the is_public status.
~~>
            from django.db import models

            class UserProfile(models.Model):
                username = models.CharField(max_length=100)
                age = models.IntegerField()
                is_public = models.BooleanField(default=True)
                def __str__(self):
                    return self.username


P2. Create ModelForm & Validation: Implement a UserProfileForm extending forms.ModelForm. Add a clean_age() method to enforce custom constraints, such as ensuring the user is over 13 years old before allowing profile creation.
~~> Model ME Jo Bhi Field Ho Usko form.ModelForm form field me Conver Karta He.

from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'age', 'is_public']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 13:
            raise forms.ValidationError("Age Not Valid")
        return age

    clean_age YeUser Form Submit Karta He Tab Autamaticaly call Hoga Aur Check Karega Ki User Ne Jo Vaue Du he Ye Valid he Ya Nahi.
     Data= Valid :To Data Databse ME Save   Or Date != Valid : Form Reject Karega


P3. Django Views for Persistence: Develop a function-based or class-based viewto handle POST requests. Use form.is_valid() to check inputs and form.save() to commit the new profile data directly to the database.
~~>
from django.shortcuts import render, redirect
from .forms import UserProfileForm

def create_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()      # Database me data save karega
            return redirect('success')   # Ya kisi page par redirect kare
    else:
        form = UserProfileForm()
    return render(request, 'create_profile.html', {'form': form})

P4. Render Profiles with DTL: Retrieve all profiles using UserProfile.objects.all() and pass them to a template. Use Django Template Language (DTL) loops ({% for profile in profiles %}) to display the username and age in an HTML list.
~~> View Me :
            from django.shortcuts import render
            from .models import UserProfile

            def profile_list(request):
                profiles = UserProfile.objects.all()
                return render(request, 'profile_list.html',{'profiles': profiles})

<!DOCTYPE html>
<html>
<head>
    <title>User Profiles</title>
</head>
    <body>
    <h2>User Profiles</h2>
    <ul>
        {% for profile in profiles %}
            <li>
                Username: {{ profile.username }}
                <br>
                Age: {{ profile.age }}
            </li>
        {% endfor %}
    </ul>
    </body>
</html>

                                                                *=*=*=*= Section C: Mini Project  *=*=*=*=  

P1. Create/Edit via Django Forms Develop a dynamic profile management system using Django ModelForms. This allows you to automatically generate HTML forms from your Profile model, handle data validation, and save user input directly to the database with minimal code.
~~> Project cretae  Karo. Uske Location Par Jakar Create App  Aur Upar Vale Model banao.Bad Me Apne Terminal Me Command 
    python manage.py makemigrations
    python manage.py migrate 
    froms.py Me :
            from django import forms
            from .models import UserProfile

            class UserProfileForm(forms.ModelForm):
                class Meta:
                    model = UserProfile
                    fields = ['username','age','is_public']

                def clean_age(self):
                    age = self.cleaned_data['age']
                    if age<13:
                        raise forms.ValidationError("Age Not Valid")
                    return age
    view.py :
            from django.shortcuts import render, redirect, get_object_or_404
            from .models import UserProfile
            from .forms import UserProfileForm

            def create_profile(request):
                if request.method == "POST":
                    form = UserProfileForm(request.POST)
                    if form.is_valid():
                        form.save()
                        return redirect('profile_list')
                else:
                    form = UserProfileForm()
                return render(request, 'profile_form.html', {'form': form})

            def edit_profile(request, id):
                profile = get_object_or_404(UserProfile, id=id)
                if request.method == "POST":
                    form = UserProfileForm(request.POST, instance=profile)
                    if form.is_valid():
                        form.save()
                        return redirect('profile_list')
                else:
                    form = UserProfileForm(instance=profile)
                return render(request, 'profile_form.html', {'form': form})                                                 
                                                                         
                                                                         
P2.Relational Database Integration Configure your app to communicate with arobust RDBMS like PostgreSQL or MySQL. Use the Django ORM to create a Profile table and implement a "List View" that queries all records from the database to display them on a central dashboardRelational Database Integration Configure your app to communicate with a robust RDBMS like PostgreSQL or MySQL. Use the Django ORM to create a Profile table and implement a "List View" that queries all records from the database to display them on a central dashboard.
~~> Jo Upar vale Project Me pip install mysqlclient karo Ke seting.py Me Ye Step Add Karenge 
                DATABASES = {
                    'default': {'ENGINE': 'django.db.backends.mysql',
                                'NAME': 'socialdb',
                                'USER': 'root',
                                'PASSWORD': 'root',
                                'HOST': 'localhost',
                                'PORT': '3306'}
                            }                                           
    Uske Bad Makemigration or Migrate Ke Commnad Run Karo.

P3."Save to File" with Context Managers Implement an export feature using Python's csv module. Use a Context Manager (with open(...) as file:) to ensure proper file handling, allowing the app to fetch database records andwrite them into a downloadable CSV file safely.
~~> view Me: 
            import csv
            from .models import UserProfile

            def export_profiles():
                profiles = UserProfile.objects.all()
                with open('profiles.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Username', 'Age', 'Is Public'])
                    for profile in profiles:
                        writer.writerow([ profile.username , profile.age , profile.is_public ])                                         
                                                                         
                                                                         
P4.Clean URL Routing & Templates Organize your application using a clear directory structure. Implement specific URL patterns for "List," "Create," and "Export" views,and use Django Template Language (DTL) to render the profile data into a clean, user-friendly interface.                                                         
~~> Vies Me :
            from django.shortcuts import render, redirect
            from django.http import HttpResponse
            from .models import UserProfile
            from .forms import UserProfileForm
            import csv


            def profile_list(request):
                profiles = UserProfile.objects.all()
                return render(request, 'profiles/profile_list.html', {'profiles': profiles})

            def create_profile(request):
                if request.method == "POST":
                    form = UserProfileForm(request.POST)
                    if form.is_valid():
                        form.save()
                        return redirect('profile_list')
                else:
                    form = UserProfileForm()
                    return render(request, 'profiles/profile_form.html', {'form': form})

            def export_profiles(request):
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="profiles.csv"'
                writer = csv.writer(response)
                writer.writerow(['Username', 'Age', 'Public'])
                for profile in UserProfile.objects.all():
                    writer.writerow([ profile.username, profile.age,profile.is_public])
                return response                                                                                                                                   
                                                                         
 """