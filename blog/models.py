from django.db import models
from django.conf import settings
from django.utils import timezone


#カテゴリのモデル
class Category(models.Model):
    name = models.CharField(
        'カテゴリ',
        max_length=100,        
        )
   
    def __str__(self):
        return self.name


#ニックネーム設定用モデル
class Nickname(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True,
    )

    def __str__(self):
        return self.nickname

#投稿記事のモデル
class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',       
        on_delete=models.PROTECT
    )

    title = models.CharField(
        "タイトル", 
        max_length=200,
        blank=False,
        null=False)
    image = models.ImageField(
        upload_to='images', 
        verbose_name='イメージ画像', 
        null=True,
        blank=True
    )

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
    
    def __str__(self):
        return self.title

#本文とimgのセット
class ContentCard(models.Model):
    content = models.TextField()
    image = models.ImageField(
        upload_to='images', 
        verbose_name='イメージ画像', 
        null=True,
        blank=True
    )
    post = models.ForeignKey(
        Post,
        related_name = "contentcard",
        on_delete = models.CASCADE
    )


