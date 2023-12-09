from django.contrib.auth.models import User
from rest_framework import serializers

from author.models import Author
from category.models import Category
from .models import Post

class PostAuthorUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class PostAuthorSerializer(serializers.ModelSerializer):
    user = PostAuthorUserSerializer(read_only=True)

    class Meta:
        model = Author
        fields = ['user']

class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug', 'name']

class PostSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    category = PostCategorySerializer(read_only=True)
    author = PostAuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
