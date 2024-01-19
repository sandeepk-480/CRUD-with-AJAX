from django.contrib import admin
from app.models import MyUser

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']

