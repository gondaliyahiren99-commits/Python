
from django.shortcuts import render
from django.http import HttpResponse
# pyrefly: ignore [missing-import]
from .models import User,Jobseeker

# Create your views here.
def login(request):
    return render(request,'jobseeker/login.html')

def register(request):
    if request.POST:
        role = request.POST['role']
        if role == 'jobseeker':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone_number = request.POST['phone_number']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            skills = request.POST['skills']
          
        
            if 'terms' in request.POST: 
                if password == confirm_password:
                    uid = User.objects.create(
                        email=email,
                        password=password,
                        role=role)
            
                    jid=Jobseeker.objects.create(
                        user_fk = uid,
                        first_name = first_name,
                        last_name = last_name,
                        phone_number = phone_number,
                        skills = skills
                    )   
                    return render(request,'jobseeker/login.html')
                else :
                    return render(request,'jobseeker/register.html')       
            else:
                pass
        elif role == 'company' :
            role = request.POST['role']
            print("Compnay register hear" ,role)

        
        return render(request,'jobseeker/register.html')
    
    else:
        return render(request,'jobseeker/register.html')