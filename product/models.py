from datetime import datetime, timedelta

from django.db import models

# Create your models here.
from user.models import User


class Event(models.Model):
    title = models.CharField("제목", max_length=50)
    thumbnail = models.ImageField("썸네일", upload_to='static/', height_field=None, width_field=None, max_length=None)
    introduction = models.CharField(max_length=200)
    create_at = models.DateTimeField("작성일", auto_now_add=True)
    activity_start_at = models.DateTimeField("노출시작일", default=datetime.now(), blank=True)
    activity_end_at = models.DateTimeField("노출종료일", default=datetime.now() + timedelta(days=3), blank=True)
    is_activity = models.BooleanField(default=True)

    def __str__(self):
        return f"이벤트 제목 : {self.title}"


class Product(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    thumbnail = models.ImageField("썸네일", upload_to='static/', height_field=None, width_field=None, max_length=None)
    introduction = models.CharField(max_length=200)
    create_at = models.DateTimeField("작성일", auto_now_add=True)
    activity_start_at = models.DateTimeField("노출시작일", default=datetime.now(), blank=True)
    activity_end_at = models.DateTimeField("노출종료일", default=datetime.now() + timedelta(days=3), blank=True)
    is_activity = models.BooleanField(default=True)


class Review(models.Model):
    writer = models.ForeignKey(User, related_name='user_review', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_review', on_delete=models.CASCADE)

