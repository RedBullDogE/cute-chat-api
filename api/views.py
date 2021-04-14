from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Message
from .serializers import MessageSerializer


class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """

    def has_permission(self, request, view):
        for klass, actions in getattr(view, "action_permissions", {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False


class MessageViewSet(ModelViewSet):
    """
    A viewset for viewing and editing messages. All users can get list of messages,
    specific message or create a new one. Only authorized users can update and destroy
    their own messages.

    list: List of messages (paginated by 10 per page)

    retrieve: Get specific message by id

    update: Rewrite entire message record

    create: Add new message

    partial_update: Rewrite specific fields of message record

    destroy: Remove specific message by id
    """

    serializer_class = MessageSerializer
    queryset = Message.objects.all().order_by("-create_date")

    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAuthenticated: ["update", "partial_update", "destroy"],
        AllowAny: ["retrieve", "list", "create"],
    }

    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def destroy(self, request, pk=None):
        message = self.get_object()
        if message.author_email == request.user.email:
            message.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("Access is denied", status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        message = self.get_object()
        if message.author_email == request.user.email:
            serializer = self.serializer_class(message, request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)
        return Response("Access is denied", status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, *args, **kwargs):
        message = self.get_object()
        if message.author_email == request.user.email:
            serializer = self.serializer_class(message, request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)
        return Response("Access is denied", status=status.HTTP_403_FORBIDDEN)
