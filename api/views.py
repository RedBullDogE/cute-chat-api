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

    list: List of messages (paginated by 10 per page)

    retrieve: Get specific message by id

    update: Rewrite entire message record

    create: Add new message

    partial_update: Rewrite specific fields of message record

    destroy: Remove specific message by id
    """

    serializer_class = MessageSerializer
    queryset = Message.objects.all()
