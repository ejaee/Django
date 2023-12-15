# users/urls.py

from django.urls import path
from .views import CreateUserView
from .views import ListUserView

urlpatterns = [
    path('users/', CreateUserView.as_view(), name='create_user'),
    path('users/user/', ListUserView.as_view()),
]
