from django.db import models

# Create your models here.
class User(models.Model):
    ROLL = (('jobseeker','jobseeker'),
            ('company','company'))
    email = models.EmailField(max_length = 30)
    password = models.CharField(max_length = 30)
    role = models.CharField(max_length=30,choices=ROLL)
    created_at =models.DateField(auto_now=True)
    def __str__(self):
        return self.email

class Jobseeker(models.Model):
    user_fk = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    phone_number = models.PositiveBigIntegerField()
    skills= models.CharField(max_length = 60)
    location = models.CharField(max_length=30, blank=True, default='')
    def __str__(self):
        return self.first_name

class Company(models.Model):
    user_fk = models.ForeignKey(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length = 30)
    company_website = models.URLField()
    industry_type = models.CharField(max_length = 30)
    company_size = models.CharField(max_length = 30)
    about_company = models.TextField()
    company_logo = models.ImageField(upload_to='company_logo')
    recruiter_name = models.CharField(max_length = 30)
    company_linkedin_url = models.URLField()
    def __str__(self):
        return self.company_name


