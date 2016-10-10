from rest_framework import serializers
from .models import *


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ("fbid", "name")


class PlayerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ("fbid", "name", "email")


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ("id", "name", "created_by", "difficulty")


class CommentCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ("id", "text", "created_by", "owner")


class CommentSerializer(serializers.ModelSerializer):
    owner = PlayerSerializer()

    class Meta:
        model = Comment
        fields = ("id", "text", "created_by", "owner")


class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("id", "owner", "artwork", "created_by")


class LikeSerializer(serializers.ModelSerializer):
    owner = PlayerSerializer()

    class Meta:
        model = Like
        fields = ("id", "owner", "created_by")


class ArtworkCreateSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)

    class Meta:
        model = Artwork
        fields = ("id", "name", "picture", "created_by", "owner", "public", "template")


class ArtworkSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)
    owner = PlayerSerializer()
    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)
    template = TemplateSerializer()

    class Meta:
        model = Artwork
        fields = ("id", "name", "picture", "created_by", "owner", "public", "comments", "likes", "template")


class PlayerFullSerializer(serializers.ModelSerializer):
    artwork_list = ArtworkSerializer(many=True)

    class Meta:
        model = Player
        fields = ("fbid", "name", "email", "artwork_list")


class RoomSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)
    artworks = ArtworkSerializer(many=True)
    template = TemplateSerializer()

    class Meta:
        model = Room
        field = ("players", "artworks",
                 "created_by", "started_by", "started", "template")