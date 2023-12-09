from rest_framework import viewsets
from rest_framework import permissions

from .serializers import PostSerializer
from .models import Post

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
