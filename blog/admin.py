from django.contrib import admin
from .models import *



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
