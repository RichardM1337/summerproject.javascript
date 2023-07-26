from django.contrib import admin
from .models import weatherQuery,weatherInput
# Register your models here.

admin.site.register(weatherQuery)
admin.site.register(weatherInput)