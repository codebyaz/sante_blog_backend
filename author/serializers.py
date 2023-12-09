from django.contrib.auth.models import User
from typing import OrderedDict
from rest_framework import serializers

from .models import Author

class UserAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class AuthorSerializer(serializers.ModelSerializer):
    user = UserAuthorSerializer()

    class Meta:
        model = Author
        fields = ['url', 'user', 'about']

    def create(self, validated_data: OrderedDict):
        user_data = validated_data.pop("user")
        user = User.objects.create(**user_data)
        user.save()

        return Author.objects.create(**validated_data, user=user)
