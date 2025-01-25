from rest_framework import serializers
from .models import User,Post
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User 

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'password']
    extra_kwargs = {'password': {'write_only': True}}
  def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password'])  # Hash the password for saving
        )
        user.save()
        return user

# for login
class LoginSerializer(serializers.Serializer):  # Change to serializers.Serializer
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        print("Received username:", username)  # Debugging line
        print("Received password:", password)  # Debugging line
        if username and password:
            try:
                user = User.objects.get(username=username)
                if not user.check_password(password):
                    raise serializers.ValidationError('Invalid username or password.')
            except User.DoesNotExist:
                raise serializers.ValidationError('User doesn\'t exist.')
        else:
            raise serializers.ValidationError('Must include "username" and "password".')

        data['user'] = user
        return data
# creating a post 
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'username', 'picture', 'bio', 'email', 'facebook_link',
            'twitter_link', 'instagram_link', 'linkedin_link', 'website',
            'created_at', 'updated_at'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        post = Post.objects.create(user=user, **validated_data)
        return post
