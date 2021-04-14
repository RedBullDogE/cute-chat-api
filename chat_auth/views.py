from django.contrib.auth.models import User
from rest_framework import generics

from .serializers import RegisterSerializer


class SignUpView(generics.CreateAPIView):
    """
    View for creating new users.
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
