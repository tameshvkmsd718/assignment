from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('users/', views.user_list, name='user_list'),
    path('new_user/', views.new_user, name='new_user'),
    path('users/<int:id>/', views.user_detail, name='user_detail'),
]
