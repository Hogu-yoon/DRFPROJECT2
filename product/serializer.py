from rest_framework import serializers

from product.models import Event, Product


class EventSerializer(serializers.ModelSerializer):
    '''
    title = models.CharField("제목", max_length=50)
    thumbnail = models.ImageField("썸네일", upload_to='static/', height_field=None, width_field=None, max_length=None)
    introduction = models.CharField(max_length=200)
    create_at = models.DateTimeField("작성일", auto_now_add=True)
    activity_start_at = models.DateTimeField("노출시작일", default=datetime.now(), blank=True)
    activity_end_at = models.DateTimeField("노출종료일", default=datetime.now() + timedelta(days=3), blank=True)
    is_activity = models.BooleanField(default=True)
    '''

    class Meta:
        model = Event
        fields = "__all__"


class CreateEventSerializer(serializers.ModelSerializer):
    '''
    thumbnail = models.ImageField(upload_to='static/')
    introduction = models.CharField(max_length=200)
    create_at = models.DateTimeField("작성일", auto_now_add=True)
    activity_start_at = models.DateTimeField("노출시작일", default=datetime.now(), blank=True)
    activity_end_at = models.DateTimeField("노출종료일", default=datetime.now()+timedelta(days=3), blank=True)
    is_activity = models.BooleanField(default=True)
    '''

    class Meta:
        # serializer에 사용될 model, field지정
        model = Event
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        # 예시 fields = ["username", "password", "fullname", "email"]
        fields = ['title', 'thumbnail', 'introduction']

    def validate(self, attrs):
        # custom validation pattern
        print(attrs)
        # if attrs.get("activity_start_at") > attrs.get("activity_end_at"):
        #     # validation에 통과하지 못할 경우 ValidationError class 호출
        #     raise serializers.ValidationError(
        #         # custom validation error message
        #         detail={"error": "이미지 게시일이 지났습니다."},
        #     )
        #
        # # validation에 문제가 없을 경우 data return
        return attrs


class ProductSerializer(serializers.ModelSerializer):
    '''
    write = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    thumbnail = models.ImageField("썸네일", upload_to='static/', height_field=None, width_field=None, max_length=None)
    introduction = models.CharField(max_length=200)
    create_at = models.DateTimeField("작성일", auto_now_add=True)
    activity_start_at = models.DateTimeField("노출시작일", default=datetime.now(), blank=True)
    activity_end_at = models.DateTimeField("노출종료일", default=datetime.now() + timedelta(days=3), blank=True)
    is_activity = models.BooleanField(default=True)
    '''

    class Meta:
        model = Product
        fields = "__all__"


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'thumbnail', 'introduction']

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):

        product = Product.objects.create(**validated_data)

        return product
