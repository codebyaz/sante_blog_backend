from rest_framework import viewsets, permissions

from .serializers import AuthorSerializer
from .models import Author

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AuthorSerializer