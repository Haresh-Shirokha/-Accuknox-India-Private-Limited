from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User, FriendRequest
from .serializers import UserSerializer, FriendRequestSerializer
from rest_framework.response import Response
from rest_framework import status

class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLoginView(TokenObtainPairView):
    pass

class FriendRequestView(generics.ListCreateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FriendRequest.objects.filter(to_user=user)

    def perform_create(self, serializer):
        from_user = self.request.user
        to_user_id = self.request.data.get('to_user')
        to_user = User.objects.get(id=to_user_id)
        if FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists():
            return Response({'error': 'Friend request already sent.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(from_user=from_user, to_user=to_user)
