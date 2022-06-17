# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from blog.models import Article
from blog.serializer import ArticleSerializer,ArticleCreateSerializer


class ArticleView(APIView):

    def get(self, request):
        articles = ArticleSerializer(instance=Article.objects.filter(writer=request.user),many=True)

        return Response(articles.data, status=status.HTTP_200_OK)

    def post(self, request):
        # request.data의 dict 형태가 **를 붙임으로써 kwargs로 들어감
        # data = {"writer": request.user.id, "data": request.data}

        a = ArticleCreateSerializer(data=request.data)
        # print(a.data)
        if a.is_valid():
            # print("dasdfasdfd",a)
            a.save(writer=self.request.user,category=request.data['category'])
            return Response(a.data)

        return Response(a.errors)
