from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('chats/',views.chats_,name="chats"),
    path('auth/',views.auth_,name="auth"),
    path('chatroom/<pk>/',views.chatroom_,name="chatroom"),
]
