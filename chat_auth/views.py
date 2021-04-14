from django.contrib.auth.models import User
from rest_framework import status, authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer


class SignUpView(CreateAPIView):
    """
    View for creating new users.
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class SignOutView(APIView):
    """
    View for signing out. Deactivates auth token of specific user.
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        token = get_object_or_404(Token, user=request.user)
        token.delete()
        return Response(status=status.HTTP_200_OK)
