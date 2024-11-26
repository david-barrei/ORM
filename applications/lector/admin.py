from django.contrib import admin

# Register your models here.
from .models import Prestamo,Lector

admin.site.register(Lector)
admin.site.register(Prestamo)