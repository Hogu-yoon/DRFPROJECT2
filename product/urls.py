from django.urls import path

from product import views

urlpatterns = [
    path('event', views.EventView.as_view()),
    path('', views.ProductView.as_view()),
]
