from rest_framework import serializers
from course.serializers import CourseSerializer
from video.serializers import VideoSerializer


class AnalyticsSerializers(serializers.Serializer):
    courses = CourseSerializer(read_only=True, many=True)
    videos = VideoSerializer(read_only=True, many=True)
