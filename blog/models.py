from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
        )
    
    def __str__(self):
        return self.name



class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    title = models.CharField(
        "タイトル", 
        max_length=200,
        blank=False,
        null=False)
    content = models.TextField(
        "本文",
        blank=True,
        null=False)
    created = models.DateTimeField(
        "作成日", 
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False)
    updated = models.DateTimeField(
        "更新日",
        auto_now=True,
        editable=False,
        blank=False,
        null=False)
    nickname = models.CharField(
        "ニックネーム", 
        default=author,
        max_length=200,
        blank=False,
        null=False
        )
    category = models.ForeignKey(
        Category,
        default="etc",
        on_delete=models.CASCADE)


    def __str__(self):
        return self.title
