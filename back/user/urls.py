from django.urls import path

from django.urls import path
from .views import user_list, user_detail

urlpatterns = [
    path('user/', user_list, name='user-list'),
    path('user/<int:pk>/', user_detail, name='user-detail'),
]
