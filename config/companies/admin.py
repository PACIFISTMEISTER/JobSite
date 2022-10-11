from django.contrib import admin
from .models import Job , Company, Category, Location

# Register your models here.

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Job)
admin.site.register(Company)
