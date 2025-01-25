from django.urls import path
from .views import  PostCreateView, PostDeleteView, PostListView, PostUpdateView, UserCreateView,LoginView, PostDetailView

urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='UserCreateView'),
    path('users/login/', LoginView.as_view(), name='LoginView'),
    path('posts/', PostListView.as_view(), name='PostListView'),
    path('posts/create/', PostCreateView.as_view(), name='PostCreateView'),
    path('posts/<str:username>/', PostDetailView.as_view(), name='PostDetailView'),  # Use username instead of ID
    path('posts/<str:username>/update/', PostUpdateView.as_view(), name='PostUpdateView'),
    path('posts/<str:username>/delete/', PostDeleteView.as_view(), name='PostDeleteView'),
]