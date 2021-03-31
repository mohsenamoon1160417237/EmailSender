from django.contrib import admin
from .models import Contact, Email


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ['email' , 'name' , 'profile_picture']
    list_filter = ['email' , 'name']




@admin.register(Email)
class FileAdmin(admin.ModelAdmin):

    list_display = ['message' , 'subject']

