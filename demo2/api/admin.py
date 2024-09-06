from django.contrib import admin
from .models import Book, AooHold, AooRegister
# Register your models here.

admin.site.register(Book)
admin.site.register(AooHold)
admin.site.register(AooRegister)