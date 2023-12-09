from rest_framework import viewsets, permissions

from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer
