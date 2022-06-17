from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from user import views

urlpatterns = [
    path('login',views.UserApiView.as_view())
]
