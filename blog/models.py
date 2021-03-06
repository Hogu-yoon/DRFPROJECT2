from django.db import models

# Create your models here.
from user.models import User


class Category(models.Model):
    name = models.CharField('카테고리이름', max_length=100)
    introduction = models.TextField("소개")

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ManyToManyField(Category, related_name="category_article")
    writer = models.ForeignKey(User, related_name="user_article", on_delete=models.CASCADE)
    title = models.CharField('글제목', max_length=200)
    article = models.TextField('글내용')
    create_at = models.DateTimeField("작성일", auto_now_add=True)
    update_at = models.DateTimeField("수정일", auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="article_comment", on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name="article_comment", on_delete=models.CASCADE)
    comment = models.TextField('댓글', max_length=500)
    create_at = models.DateTimeField("작성일", auto_now_add=True)
    update_at = models.DateTimeField("수정일", auto_now=True)

    def __str__(self):
        return self.writer
