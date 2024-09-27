from django.urls import path
from .views import UserSignupView, UserLoginView, FriendRequestView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('friend-requests/', FriendRequestView.as_view(), name='friend-requests'),
]