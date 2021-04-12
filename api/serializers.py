from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    """
    Basic serializer for the Message model for all fields.
    """
    class Meta:
        model = Message
        fields = "__all__"
