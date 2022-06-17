from rest_framework import serializers

from blog.models import Article, Category, Comment
from user.serializer import UserSerializer
from user.models import User


class CommentSerializer(serializers.ModelSerializer):
    '''
        article = models.ForeignKey(Article, related_name="article_comment", on_delete=models.CASCADE)
        writer = models.ForeignKey(User, related_name="article_comment", on_delete=models.CASCADE)
        comment = models.TextField('댓글', max_length=500)
        create_at = models.DateTimeField("작성일", auto_now_add=True)
        update_at = models.DateTimeField("수정일", auto_now=True)
    '''

    class Meta:
        model = Comment
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    '''
    name = models.CharField('카테고리이름', max_length=100)
    introduction = models.TextField("소개")
    '''

    class Meta:
        model = Category
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    '''
       category = models.ManyToManyField(Category, related_name="category_article")
       writer = models.ForeignKey(User, related_name="user_article", on_delete=models.CASCADE)
       title = models.CharField('글제목', max_length=200)
       article = models.TextField('글내용')
       create_at = models.DateTimeField("작성일", auto_now_add=True)
       update_at = models.DateTimeField("수정일", auto_now=True)
   '''
    # writer = UserSerializer()
    # readonlyfield를 사용할때는 사용모델의 외래키 필드 명이나 related명으로 참조
    writer = serializers.ReadOnlyField(source='writer.username')
    category = CategorySerializer(many=True, required=False)

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
        categories = validated_data.pop("category")
        a = Article.objects.create(**validated_data)
        a.category.add(*categories)
        return a

    def update(self, instance, validated_data):
        pass

# https://stackoverflow.com/questions/6996176/how-to-create-an-object-for-a-django-model-with-a-many-to-many-field
