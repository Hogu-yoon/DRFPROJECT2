from django.shortcuts import render

# Create your views here.
# partial=True 이것은 required=False 같은 그런 그것
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Event, Product
from product.serializer import EventSerializer, CreateEventSerializer, ProductSerializer, CreateProductSerializer


class EventView(APIView):
    def get(self, request):
        return Response(EventSerializer(Event.objects.all().last()).data, status=status.HTTP_200_OK)

    # 생성
    def post(self, request):
        event_serializer = CreateEventSerializer(data=request.data)
        if event_serializer.is_valid(raise_exception=True):
            event_serializer.save()

            return Response(event_serializer.data, status=status.HTTP_201_CREATED)

    # 수정
    def put(self, request, obj_id):

        product = Event.objects.get(id=obj_id)

        event_serializer = CreateEventSerializer(product, data=request.data, partial=True)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):

    def get(self, request):
        return Response(ProductSerializer(Product.objects.all().last()).data, status=status.HTTP_200_OK)

    def post(self, request):
        product_serializer = CreateProductSerializer(data=request.data)
        if product_serializer.is_valid(raise_exception=True):
            product_serializer.save(writer=request.user)

            return Response(product_serializer.data, status=status.HTTP_201_CREATED)
