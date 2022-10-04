from django.contrib import admin
from .models import Post, Category, ContentCard



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ContentCard)
class ContentCardAdmin(admin.ModelAdmin):
    pass