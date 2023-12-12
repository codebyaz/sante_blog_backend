from rest_framework import serializers

from post.serializers import PostAuthorSerializer, PostCategorySerializer
from post.models import Post
from .models import Category

class CategoryPostSerializer(serializers.ModelSerializer):
    author = PostAuthorSerializer()
    category = PostCategorySerializer()

    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'slug', 'author', 'category', 'reading_duration', 'created_at']

class CategorySerializer(serializers.ModelSerializer):
    posts = CategoryPostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'slug', 'posts']
