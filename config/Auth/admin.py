from django.contrib import admin

# Register your models here.
from .models import CompanyUser, AverageUser

admin.site.register(CompanyUser)

admin.site.register(AverageUser)
