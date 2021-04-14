from django.urls import path
from rest_framework.authtoken import views

from .views import SignUpView, SignOutView

urlpatterns = [
    path("signin/", views.obtain_auth_token),
    path("signup/", SignUpView.as_view()),
    path("signout/", SignOutView.as_view()),
]
