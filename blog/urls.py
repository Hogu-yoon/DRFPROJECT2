from django.urls import path

from blog import views

urlpatterns = [
    path('article', views.ArticleListView.as_view()),
    path('article/<int:article_id>', views.ArticleView.as_view()),
    path('article/my-post', views.UserArticleView.as_view()),
]