from rest_framework import viewsets
from .serializers import LibraryPermissionSerializer
from .models import LibraryPermission

class LibraryPermissionViewSet(viewsets.ModelViewSet):
    queryset = LibraryPermission.objects.all()
    serializer_class = LibraryPermissionSerializer