from django.urls import path
from users.views import UserSignupView, UserLoginView, FriendRequestView

urlpatterns = [
    path('api/signup/', UserSignupView.as_view(), name='signup'),
    path('api/login/', UserLoginView.as_view(), name='login'),
    path('api/friend-requests/', FriendRequestView.as_view(), name='friend-requests'),
]