from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status,generics,permissions
from .models import User,Post
from .serializers import UserSerializer,LoginSerializer,PostSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


# Createing view for registration
class UserCreateView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

#creating view for Login
class LoginView(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request,  *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception = True)
    user = serializer.validated_data['user']

    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh' : str(refresh),
      'access' : str(refresh.access_token),
    }, status=status.HTTP_200_OK)
  
#creating a view
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        username = self.kwargs.get('username')
        return get_object_or_404(Post, user__username=username)

class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Post, user__username=self.request.user.username)

class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Post, user__username=self.request.user.username)