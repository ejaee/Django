from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index), # ''로 들어왔을 때 views.index 가 실행된다
    path('create/', views.create),
    path('read/<id>/', views.read),
    path('update/<id>/', views.update),
    path('delete/', views.delete)
]
