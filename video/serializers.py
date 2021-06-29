
from .models import Video, Tag
from rest_framework import serializers


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        exclude = ()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ()

