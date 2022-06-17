from datetime import datetime, timedelta

from django.db import models

# Create your models here.
class Event(models.Model):
    thumbnail = models.ImageField(upload_to='static/')
    introduction = models.CharField(max_length=200)
    create_at = models.DateTimeField("작성일", auto_now_add=True)
    activity_start_at = models.DateTimeField("노출시작일", default=datetime.now(), blank=True)
    activity_end_at = models.DateTimeField("노출종료일", default=datetime.now()+timedelta(days=3), blank=True)
    is_activity = models.BooleanField(default=True)

