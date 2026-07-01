from django.contrib import admin

# Register your models here.
# pyrefly: ignore [missing-import]
from .models import User,Jobseeker,Company

admin.site.register(User)
admin.site.register(Jobseeker)
admin.site.register(Company)
