from rest_framework import serializers

from blog.models import Article, Category
from user.serializer import UserSerializer
from user.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    writer = UserSerializer()
    category = CategorySerializer(many=True)

    class Meta:
        # serializer에 사용될 model, field지정
        model = Article
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        # fields = ["username", "password", "fullname", "email"]
        fields = "__all__"

    # def validate(self, attrs):
    #
    #
    # def create(self, validated_data):
    #     Article.objects.create(writer=request.)


class ArticleCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Article
        fields = ['title', 'article']

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        categorys = validated_data.pop("category")
        writer = validated_data.pop("writer")
        writer = User.objects.get(id=writer.id)
        a = Article.objects.create(writer=writer,**validated_data)
        print(categorys)
        for x in categorys:
            a.category.add(x)
        return a

    def update(self, instance, validated_data):
        pass


# https://stackoverflow.com/questions/6996176/how-to-create-an-object-for-a-django-model-with-a-many-to-many-field