from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.


# class ArtworkList(generics.ListCreateAPIView):
#     queryset = Artwork.objects.all()
#     serializer_class = ArtworkSerializer


class ArtworkDetail(generics.RetrieveAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerFullSerializer


class ArtworkCreate(generics.CreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkCreateSerializer


class UserCreate(generics.CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerCreateSerializer

class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer


class LikeCreate(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeCreateSerializer


# class CommentListInArtwork(generics.ListAPIView):
#     queryset = ArtworkList.object.get(pk=self.kwargs.get('pk')).comments
#     serializer_class = CommentSerializer
#
# class CommentListInArtwork(generics.ListAPIView):
#     queryset = ArtworkList.object.get(pk=self.kwargs.get('pk')).comments
#     serializer_class = CommentSerializer

