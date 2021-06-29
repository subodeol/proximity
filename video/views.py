from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Video, Tag
from .serializers import VideoSerializer, TagSerializer
from rest_framework import viewsets
from school.permissions import IsInstructer, IsStudent
from rest_framework.response import Response
import logging
logger = logging.getLogger(__name__)



class VideoViewSet(viewsets.ModelViewSet):
    # permissions required
    permission_classes = [IsAuthenticated]      
    # queryset
    queryset = Video.objects.all()
    # serializer to be used
    serializer_class = VideoSerializer

    def get_permissions(self):
        logger.info("Checking permissions for Video view")
        """Set custom permissions for each action."""
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            self.permission_classes = [IsInstructer, ]
        elif self.action in ['get']:
            self.permission_classes = [IsStudent, ]
        return super().get_permissions()

    def retrieve(self, request, pk=None):
        try:
            video_object = Video.objects.get(id=pk)
            video_object.total_views += 1
            video_object.save()
            serializer = self.get_serializer(video_object)
            logger.info("total_views for video "+video_object.name+" is increased by 1.")
            return Response(serializer.data)
        except Exception as e:
            logger.error(e)


class TagViewSet(viewsets.ModelViewSet):
    # permissions required
    permission_classes = [IsAuthenticated]      
    # queryset
    queryset = Tag.objects.all()
    # serializer to be used
    serializer_class = TagSerializer

    def get_permissions(self):
        logger.info("Checking permissions for Tag view")
        """Set custom permissions for each action."""
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            self.permission_classes = [IsInstructer, ]
        elif self.action in ['list']:
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()