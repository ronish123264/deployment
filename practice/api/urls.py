from django.shortcuts import render
from django.urls import path
from . import views



app_name = 'api'
urlpatterns = [
    path('', views.PostListCreateAPIView.as_view(), name='postlistcreate'),
    path('<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='retrieveupdatedestroy'),
]