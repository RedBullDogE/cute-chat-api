from django.core.paginator import EmptyPage, Paginator
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet

from .models import Message
from .serializers import MessageSerializer


class MessageViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    serializer_class = MessageSerializer
    queryset = Message.objects.all()
