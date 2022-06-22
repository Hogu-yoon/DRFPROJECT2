# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from blog.models import Article
from blog.serializer import ArticleSerializer, ArticleCreateSerializer


class ArticleListView(APIView):

    def get(self, request):
        articles = ArticleSerializer(instance=Article.objects.filter(writer=request.user), many=True)

        return Response(articles.data, status=status.HTTP_200_OK)

    def post(self, request):
        # request.data의 dict 형태가 **를 붙임으로써 kwargs로 들어감
        # *를 붙임으로써 args로 들어감

        # print(type(eval(request.data["categories"])))

        a = ArticleCreateSerializer(data=request.data)
        if a.is_valid():
            a.save(writer=self.request.user, categories=eval(request.data["categories"]))
            return Response(a.data)

        return Response(a.errors)


class ArticleView(APIView):

    def get(self, request, article_id):
        article = ArticleSerializer(instance=Article.objects.get(id=article_id))

        return Response(article.data, status=status.HTTP_200_OK)


class UserArticleView(APIView):

    def get(self, request):
        # 반드시 하나이상의 쿼리셋일때는 many=True
        articles = ArticleSerializer(instance=Article.objects.filter(writer=request.user), many=True)

        return Response(articles.data, status=status.HTTP_200_OK)
