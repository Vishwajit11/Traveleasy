from django.contrib import admin

# # Register your models here.
from .models import Destination

admin.site.register(Destination)

# python manage.py makemigrations
# python manage.py migrate