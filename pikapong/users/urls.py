# users/urls.py

from django.urls import path
from .views import CreateUserView, ListUserView, RegisterView

urlpatterns = [
    path('', CreateUserView.as_view(), name='create_user'),
    path('list/', ListUserView.as_view()),

    path('register/', RegisterView.as_view()),
]
