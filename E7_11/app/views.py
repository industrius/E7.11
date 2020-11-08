from django.shortcuts import render
from .models import Advert, Comment, Tag
from .serializers import AdvertSerializer, CommentSerializer, TagSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


class AdvertList(generics.ListCreateAPIView):
    """
    GET Вывод всего списка объявлений
    POST Создание нового объявления
    JSON 
    {
        "author": "",
        "advert": ""
    }
    """
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer


class AdvertDetail(generics.RetrieveAPIView):
    """
    GET/pk Вывод одного объявления по pk
    """
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer


class CommentCreate(generics.CreateAPIView):
    """
    POST Добавить коментарий к объявлению
    JSON
    {
        "author": "",
        "comment": "",
        "advert": advert_id
    }
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TagCreate(generics.CreateAPIView):
    """
    POST Добавить тэг к объявлениям
    JSON
    {
        "title": "",
        "advert": [advert_id, advert_id, ]
    }
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class GetStat(APIView):
    """
    GET статистика для данного объявления: 
    сколько у него тегов и комментариев с помощью GET 
    запроса к серверу
    """
    def get(self, request, pk):
        advert = Advert.objects.get(id=pk)
        return Response({"comments":len(advert.comments.all()), "tags":len(advert.tags.all())})